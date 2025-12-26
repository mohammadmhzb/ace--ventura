import math
from typing import List, Dict


def dot_product(a: List[float], b: List[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def norm(v: List[float]) -> float:
    return math.sqrt(dot_product(v, v))


def cosine_similarity(a: List[float], b: List[float]) -> float:
    if norm(a) == 0 or norm(b) == 0:
        return 0.0
    return dot_product(a, b) / (norm(a) * norm(b))


def euclidean_distance(a: List[float], b: List[float]) -> float:
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def angle_between(a: List[float], b: List[float]) -> float:
    cos = cosine_similarity(a, b)
    cos = max(min(cos, 1), -1)
    return round(math.degrees(math.acos(cos)), 2)


def cosine_with_steps(a: List[float], b: List[float]) -> Dict:
    dot = dot_product(a, b)
    norm_a = norm(a)
    norm_b = norm(b)

    if norm_a == 0 or norm_b == 0:
        cosine = 0.0
    else:
        cosine = dot / (norm_a * norm_b)

    angle = math.degrees(math.acos(max(min(cosine, 1), -1)))

    return {
        "dot_product": round(dot, 3),
        "norm_user": round(norm_a, 3),
        "norm_item": round(norm_b, 3),
        "cosine_similarity": round(cosine, 3),
        "angle": round(angle, 2)
    }
