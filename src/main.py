"""CLI runner for the Music Recommender Simulation."""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "likes_acoustic": False,
    }

    print(f"\nUser profile: {user_prefs}")
    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    print(f"{'#':<3}{'Title':<28}{'Artist':<20}{'Score':>6}")
    print("-" * 70)
    for i, (song, score, explanation) in enumerate(recommendations, 1):
        print(f"{i:<3}{song['title']:<28}{song['artist']:<20}{score:>6.2f}")
        print(f"   Because: {explanation}\n")


if __name__ == "__main__":
    main()
