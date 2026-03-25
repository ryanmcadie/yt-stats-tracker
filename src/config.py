import os
from dotenv import load_dotenv

def get_api_key():
    load_dotenv()
    api_key = os.getenv("YOUTUBE_API_KEY")
    if not api_key:
        raise ValueError("Missing YOUTUBE_API_KEY in .env")
    return api_key