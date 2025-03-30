from langchain_community.tools import Tool
from langchain_community.llms import FakeLLM  # 실제 구현시 적절한 LLM으로 교체
from .retriever import PersonalLawRetriever
from .processor import InformationProcessor
from .workflow import WorkflowBuilder

class PersonalInfoLawAgent:
    def __init__(self):
        # 의존성 주입
        self.llm = FakeLLM()  # 실제 사용시 LLM 초기화
        self.search_tool = Tool(name="personal_law_search")  # 실제 검색 도구로 교체
        
        # 컴포넌트 초기화
        self.retriever = PersonalLawRetriever(self.search_tool)
        self.processor = InformationProcessor(self.llm)
        self.workflow = WorkflowBuilder(self.retriever, self.processor).build()
        
    def run(self, question: str):
        inputs = {"question": question}
        return self.workflow.stream(inputs)
    
    def visualize(self):
        return self.workflow.get_graph().draw_mermaid_png()