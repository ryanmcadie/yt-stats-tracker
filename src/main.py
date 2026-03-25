from parser import parse_channel_input
from youtube_api import get_channel_stats
from storage import save_snapshot, get_previous_snapshot, calculate_growth

def format_number(value):
    return f"{value:,}"

def main():
    user_input = input("Enter YouTube channel ID, handle, username, or URL: ").strip()

    channel_lookup = parse_channel_input(user_input)
    stats = get_channel_stats(channel_lookup)
    save_snapshot(stats)

    print("\nChannel Stats")
    print(f"Title: {stats['title']}")
    print(f"Subscribers: {format_number(stats['subscribers'])}")
    print(f"Views: {format_number(stats['views'])}")
    print(f"Videos: {format_number(stats['videos'])}")
    print("\nSnapshot saved to data/snapshots.csv")

    previous, current = get_previous_snapshot(stats["channel_id"])
    growth = calculate_growth(previous, current)

    if growth:
        print("\nSince last snapshot:")
        print(f"Subscribers: {growth['subscribers']:+,}")
        print(f"Views: {growth['views']:+,}")
        print(f"Videos: {growth['videos']:+,}")
    else:
        print("\nNo previous snapshot found for this channel yet.")

if __name__ == "__main__":
    main()
