import csv
from pathlib import Path

from app.models import Movie

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_PATH = BASE_DIR / "data" / "movies.csv"

def load_movies():
    movies = []

    with open(DATASET_PATH, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            features = [
                float(row["action"]),
                float(row["comedy"]),
                float(row["drama"]),
                float(row["scifi"]),
                float(row["romance"]),
                float(row["thriller"]),
                float(row["fantasy"]),
                float(row["mystery"]),
            ]
            movies.append(Movie(title=row["title"], features=features))

    return movies
