from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    api_key = os.getenv("YOUTUBE_API_KEY")

    if not api_key:
        print("Missing YOUTUBE_API_KEY in .env")
        return

    print("Project setup is working.")
    print(f"API key loaded: {api_key[:5]}...")

if __name__ == "__main__":
    main()
