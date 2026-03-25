from youtube_api import get_channel_stats
from storage import save_snapshot

def main():
    channel_id = input("Enter YouTube channel ID: ").strip()
    stats = get_channel_stats(channel_id)
    save_snapshot(stats)

    print("\nChannel Stats")
    print(f"Title: {stats['title']}")
    print(f"Subscribers: {stats['subscribers']}")
    print(f"Views: {stats['views']}")
    print(f"Videos: {stats['videos']}")
    print("\nSnapshot saved to data/snapshots.csv")

if __name__ == "__main__":
    main()
