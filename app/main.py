from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.dataset import load_movies
from app.recommender import recommend
from app.schemas import UserPreference

app = FastAPI(title="Ace Ventura – Recommendation Detective")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

movies = load_movies()

@app.post("/recommend")
def get_recommendations(user: UserPreference):
    user_vector = [
        user.action,
        user.comedy,
        user.drama,
        user.scifi,
        user.romance,
        user.thriller,
        user.fantasy,
        user.mystery
    ]

    return {
        "user_vector": user_vector,
        "education_mode": user.education_mode,
        "recommendations": recommend(
            user_vector,
            movies,
            education_mode=user.education_mode
        )
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=False
    )
