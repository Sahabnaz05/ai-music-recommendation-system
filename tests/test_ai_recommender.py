
import pytest

from src.recommender import load_songs
from src.ai_recommender import AIMusicRecommender


@pytest.fixture
def ai_model():
    songs = load_songs("data/songs.csv")
    return AIMusicRecommender(songs)


def test_ai_returns_five_songs(ai_model):
    results = ai_model.recommend_similar("Sunrise City", k=5)

    assert len(results) == 5


def test_ai_does_not_recommend_same_song(ai_model):
    results = ai_model.recommend_similar("Sunrise City", k=5)

    titles = [song["title"] for song in results]

    assert "Sunrise City" not in titles


def test_ai_rejects_unknown_song(ai_model):
    with pytest.raises(ValueError):
        ai_model.recommend_similar("Not A Real Song")


def test_ai_rejects_invalid_k(ai_model):
    with pytest.raises(ValueError):
        ai_model.recommend_similar("Sunrise City", k=-1)
