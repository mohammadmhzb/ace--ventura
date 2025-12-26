import math
from typing import List

def dot_product(a: List[float], b: List[float]) -> float:
    return sum(x * y for x, y in zip(a, b))

def norm(v: List[float]) -> float:
    return math.sqrt(dot_product(v, v))

def cosine_similarity(a: List[float], b: List[float]) -> float:
    if norm(a) == 0 or norm(b) == 0:
        return 0.0
    return dot_product(a, b) / (norm(a) * norm(b))
