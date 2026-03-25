import requests
from config import get_api_key

BASE_URL = "https://www.googleapis.com/youtube/v3/channels"

def get_channel_stats(channel_lookup):
    params = {
        "part": "snippet,statistics",
        "key": get_api_key(),
    }

    if channel_lookup["type"] == "id":
        params["id"] = channel_lookup["value"]
    elif channel_lookup["type"] == "handle":
        params["forHandle"] = channel_lookup["value"]
    elif channel_lookup["type"] == "username":
        params["forUsername"] = channel_lookup["value"]
    else:
        raise ValueError("Unsupported channel input type")

    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    items = data.get("items", [])
    if not items:
        raise ValueError("No channel found")

    channel = items[0]
    return {
        "channel_id": channel["id"],
        "title": channel["snippet"]["title"],
        "subscribers": int(channel["statistics"].get("subscriberCount", 0)),
        "views": int(channel["statistics"].get("viewCount", 0)),
        "videos": int(channel["statistics"].get("videoCount", 0)),
    }
