from pydantic import BaseModel, Field
from typing import List

class EducatorOutput(BaseModel):
    """Output from Agent 1 (The Educator)"""
    question: str = Field(..., description="The mathematical question text. Must use LaTeX for formulas (e.g. $x^2 + y^2$).")
    correct_answer_text: str = Field(..., description="The text of the correct answer, not just a letter.")
    explanation: str = Field(..., description="A step-by-step diagnostic explanation of how to solve the problem.")

class Distractor(BaseModel):
    """A single plausible distractor and the misconception it targets"""
    distractor_text: str = Field(..., description="The incorrect mathematical answer.")
    misconception: str = Field(..., description="The common student error that leads to this incorrect answer.")

class SpecialistOutput(BaseModel):
    """Output from Agent 2 (The Misconception Specialist)"""
    distractors: List[Distractor] = Field(..., description="Exactly three plausible incorrect answers based on common student misconceptions.", min_items=3, max_items=3)

class FinalMCQ(BaseModel):
    """The final structured MCQ after combining Agent 1 and Agent 2"""
    question: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_answer: str = Field(..., description="The letter of the correct option: A, B, C, or D.")
    explanation: str
