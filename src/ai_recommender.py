
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler


class AIMusicRecommender:
    """Recommend similar songs using machine learning."""

    FEATURES = [
        "energy",
        "danceability",
        "valence",
        "acousticness"
    ]

    def __init__(self, songs):
        if not songs:
            raise ValueError("The song dataset cannot be empty.")

        self.songs = songs

        self.scaler = StandardScaler()

        self.features = np.array([
            [float(song[feature]) for feature in self.FEATURES]
            for song in songs
        ])

        self.scaled_features = self.scaler.fit_transform(
            self.features
        )

        self.model = NearestNeighbors(
            metric="euclidean"
        )

        self.model.fit(self.scaled_features)

    def recommend_similar(self, song_title, k=5):
        """Find songs with similar musical characteristics."""

        if not isinstance(k, int) or isinstance(k, bool) or k < 1:
            raise ValueError("k must be a positive integer.")

        matching_indices = [
            i for i, song in enumerate(self.songs)
            if song["title"].casefold() == song_title.casefold()
        ]

        if not matching_indices:
            raise ValueError("Song not found in the dataset.")

        song_index = matching_indices[0]

        count = min(k + 1, len(self.songs))

        distances, indices = self.model.kneighbors(
            self.scaled_features[song_index].reshape(1, -1),
            n_neighbors=count
        )

        recommendations = []

        for distance, index in zip(
            distances[0], indices[0]
        ):
            if index == song_index:
                continue

            song = self.songs[index]

            recommendations.append({
                "title": song["title"],
                "artist": song["artist"],
                "distance": round(float(distance), 3)
            })

            if len(recommendations) == k:
                break

        return recommendations
