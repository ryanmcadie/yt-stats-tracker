import requests
from config import get_api_key

BASE_URL = "https://www.googleapis.com/youtube/v3/channels"

def get_channel_stats(channel_id):
    params = {
        "part": "snippet,statistics",
        "id": channel_id,
        "key": get_api_key(),
    }
    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    items = data.get("items", [])
    if not items:
        raise ValueError("No channel found for that ID")

    channel = items[0]
    return {
        "channel_id": channel["id"],
        "title": channel["snippet"]["title"],
        "subscribers": channel["statistics"].get("subscriberCount", "0"),
        "views": channel["statistics"].get("viewCount", "0"),
        "videos": channel["statistics"].get("videoCount", "0"),
    }
