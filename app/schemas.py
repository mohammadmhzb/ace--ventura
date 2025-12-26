from typing import List
from pydantic import BaseModel

class UserPreference(BaseModel):
    action: float
    comedy: float
    drama: float
    scifi: float

class RecommendationResponse(BaseModel):
    title: str
    score: float
