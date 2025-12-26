from dataclasses import dataclass
from typing import List

@dataclass
class Movie:
    title: str
    features: List[float]
