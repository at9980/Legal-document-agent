from langgraph.graph import StateGraph, END
from .models import PersonalRagState

class WorkflowBuilder:
    def __init__(self, retriever, processor):
        self.retriever = retriever
        self.processor = processor
        
    def _should_continue(self, state: PersonalRagState) -> str:
        if state["num_generations"] >= 2:
            return "end"
        if len(state["extracted_info"]) >= 1:
            return "end"
        return "continue"
    
    def build(self) -> StateGraph:
        workflow = StateGraph(PersonalRagState)
        
        # 노드 추가
        workflow.add_node("retrieve", self.retriever.retrieve_documents)
        workflow.add_node("extract", self.processor.extract_and_evaluate)
        workflow.add_node("rewrite", self.processor.rewrite_query)
        workflow.add_node("generate", self.processor.generate_answer)
        
        # 엣지 연결
        workflow.add_edge("retrieve", "extract")
        workflow.add_conditional_edges(
            "extract",
            self._should_continue,
            {"continue": "rewrite", "end": "generate"}
        )
        workflow.add_edge("rewrite", "retrieve")
        workflow.add_edge("generate", END)
        
        return workflow.compile()