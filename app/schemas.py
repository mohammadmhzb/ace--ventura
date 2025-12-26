from pydantic import BaseModel
from typing import Literal

class UserPreference(BaseModel):
    action: float
    comedy: float
    drama: float
    scifi: float
    metric: Literal["cosine", "euclidean"] = "cosine"
    education_mode: bool = False
