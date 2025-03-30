from pydantic import BaseModel, Field
from typing import List, TypedDict, Optional

class InformationStrip(BaseModel):
    """추출된 정보에 대한 내용과 출처, 관련성 점수"""
    content: str = Field(..., description="추출된 정보 내용")
    source: str = Field(..., description="정보의 출처(법률 조항 또는 URL 등)")
    relevance_score: float = Field(..., ge=0, le=1, description="관련성 점수")
    faithfulness_score: float = Field(..., ge=0, le=1, description="충실성 점수")

class ExtractedInformation(BaseModel):
    strips: List[InformationStrip] = Field(..., description="추출된 정보 조각들")
    query_relevance: float = Field(..., ge=0, le=1, description="답변 가능성 점수")

class RefinedQuestion(BaseModel):
    """개선된 질문과 이유"""
    question_refined : str = Field(..., description="개선된 질문")
    reason : str = Field(..., description="이유")

class CorrectiveRagState(TypedDict):
    question: str
    generation: str
    documents: List[Document]
    num_generations: int

class PersonalRagState(CorrectiveRagState):
    rewritten_query: str
    extracted_info: Optional[ExtractedInformation]
    node_answer: Optional[str]