from pydantic import BaseModel
from typing import Literal

class UserPreference(BaseModel):
    action: float
    comedy: float
    drama: float
    scifi: float
    romance: float
    thriller:float
    fantasy:float
    mystery:float
    metric: Literal["cosine", "euclidean"] = "cosine"
    education_mode: bool = False
