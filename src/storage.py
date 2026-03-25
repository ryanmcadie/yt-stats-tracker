import csv
import os
from datetime import datetime, timezone

FILE_PATH = "data/snapshots.csv"
FIELDNAMES = ["timestamp", "channel_id", "title", "subscribers", "views", "videos"]

def save_snapshot(stats):
    os.makedirs("data", exist_ok=True)
    file_exists = os.path.isfile(FILE_PATH)

    with open(FILE_PATH, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "channel_id": stats["channel_id"],
            "title": stats["title"],
            "subscribers": stats["subscribers"],
            "views": stats["views"],
            "videos": stats["videos"],
        })

def load_channel_history(channel_id):
    if not os.path.exists(FILE_PATH):
        return []

    rows = []
    with open(FILE_PATH, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["channel_id"] == channel_id:
                row["subscribers"] = int(row["subscribers"])
                row["views"] = int(row["views"])
                row["videos"] = int(row["videos"])
                rows.append(row)

    return rows

def get_previous_snapshot(channel_id):
    history = load_channel_history(channel_id)
    if len(history) < 2:
        return None, None
    return history[-2], history[-1]

def calculate_growth(previous, current):
    if not previous or not current:
        return None

    return {
        "subscribers": current["subscribers"] - previous["subscribers"],
        "views": current["views"] - previous["views"],
        "videos": current["videos"] - previous["videos"],
    }
