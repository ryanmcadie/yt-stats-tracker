import csv
import os
from datetime import datetime

FILE_PATH = "data/snapshots.csv"

def save_snapshot(stats):
    os.makedirs("data", exist_ok=True)
    file_exists = os.path.isfile(FILE_PATH)

    with open(FILE_PATH, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["timestamp", "channel_id", "title", "subscribers", "views", "videos"])
        writer.writerow([
            datetime.utcnow().isoformat(),
            stats["channel_id"],
            stats["title"],
            stats["subscribers"],
            stats["views"],
            stats["videos"],
        ])
