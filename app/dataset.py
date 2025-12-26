import csv
from app.models import Movie

DATASET_PATH = "data/movies.csv"

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
            ]
            movies.append(Movie(title=row["title"], features=features))

    return movies
