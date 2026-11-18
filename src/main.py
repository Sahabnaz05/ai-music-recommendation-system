
"""
Command line runner for the Music Recommender Simulation.
"""

from .recommender import load_songs, recommend_songs
from .ai_recommender import AIMusicRecommender
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


def main() -> None:
    logging.info("Starting Music Recommendation System")

    songs = load_songs("data/songs.csv")

    logging.info("Successfully loaded %d songs", len(songs))

    print(f"Loaded songs: {len(songs)}")


    recommender = AIMusicRecommender(songs)

    user_profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.85
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.35
        },
        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.95
        },
        "Conflicting Sad Energy": {
            "genre": "r&b",
            "mood": "sad",
             "energy": 0.95
        }
    }

    for profile_name, user_prefs in user_profiles.items():
        print(f"\n--- {profile_name} ---")

        recommendations = recommend_songs(
            user_prefs, songs, k=5
        )

        for i, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec

            print(f"{i}. {song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


    # AI-powered song recommendations
    print("\n=== AI MUSIC RECOMMENDATIONS ===")

    ai_model = AIMusicRecommender(songs)

    recommendations = ai_model.recommend_similar(
        "Sunrise City", k=5
    )

    for song in recommendations:
        print(
            f"{song['title']} by {song['artist']}"
        )

if __name__ == "__main__":
    main()
