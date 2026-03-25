# YouTube Stats Tracker

A Python CLI app that fetches YouTube channel statistics, stores timestamped snapshots locally, and reports growth between checks.

## Features

- Track a YouTube channel by channel ID, handle, username, or URL
- Fetch channel title, subscriber count, total views, and public video count
- Save each fetch as a local CSV snapshot
- Compare the latest snapshot to the previous one and show growth

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/ryanmcadie/yt-stats-tracker.git
cd yt-stats-tracker
```
### 2. Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Create your env file
Copy .env.example to .env and add your YouTube API key:

```text
YOUTUBE_API_KEY=your_real_api_key_here
```
Run
```bash
python src/main.py
```