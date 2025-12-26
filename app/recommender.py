from typing import List
from app.models import Movie
from app.vector_utils import cosine_with_steps, norm, euclidean_distance

def recommend(user_vector: List[float], movies: List[Movie], education_mode=False):
    results = []

    for movie in movies:
        analysis = cosine_with_steps(user_vector, movie.features)

        results.append({
            "title": movie.title,
            "score": analysis["cosine_similarity"],
            "angle": analysis["angle"],
            "analysis": analysis if education_mode else None
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:3]
