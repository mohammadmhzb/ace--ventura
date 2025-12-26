from typing import List
from app.models import Movie
from app.vector_utils import cosine_similarity

def recommend(
    user_vector: List[float],
    movies: List[Movie],
    top_n: int = 3
):
    scores = []

    for movie in movies:
        similarity = cosine_similarity(user_vector, movie.features)
        scores.append({
            "title": movie.title,
            "score": round(similarity, 3)
        })

    scores.sort(key=lambda x: x["score"], reverse=True)
    return scores[:top_n]
