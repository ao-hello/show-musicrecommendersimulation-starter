"""CLI runner for the Music Recommender Simulation."""

from src.recommender import load_songs, recommend_songs


PROFILES = {
    "High-Energy Pop": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.85,
        "likes_acoustic": False,
    },
    "Chill Lofi": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.35,
        "likes_acoustic": True,
    },
    "Deep Intense Rock": {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.9,
        "likes_acoustic": False,
    },
    "Adversarial: Conflicted Listener": {
        "genre": "pop",
        "mood": "sad",
        "energy": 0.9,
        "likes_acoustic": True,
    },
}


def print_recs(name: str, user_prefs: dict, songs: list) -> None:
    print(f"\n=== {name} ===")
    print(f"Profile: {user_prefs}")
    recommendations = recommend_songs(user_prefs, songs, k=5)
    print(f"\n{'#':<3}{'Title':<28}{'Artist':<20}{'Score':>6}")
    print("-" * 70)
    for i, (song, score, explanation) in enumerate(recommendations, 1):
        print(f"{i:<3}{song['title']:<28}{song['artist']:<20}{score:>6.2f}")
        print(f"   Because: {explanation}\n")


def main() -> None:
    songs = load_songs("data/songs.csv")
    for name, prefs in PROFILES.items():
        print_recs(name, prefs, songs)


if __name__ == "__main__":
    main()
