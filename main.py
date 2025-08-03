import sys
import urllib.request
import json
from datetime import datetime



if len(sys.argv) < 2:
    print("you must type GitHub username after python main.py [username]")
    sys.exit(1)

username = sys.argv[1]
url = f"https://api.github.com/users/{username}/events"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

try:
    with urllib.request.urlopen(req) as response:
        data = response.read()
        events = json.loads(data)
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code} - {e.reason}")
    sys.exit(1)
except urllib.error.URLError as e:
    print(f"URL Error: {e.reason}")
    sys.exit(1)


for event in events[:5]:
    event_type = event["type"]
    repo = event["repo"]["name"]
    date_str = event["created_at"]
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
    formatted_date = date_obj.strftime("%d %b %Y %H:%M")
    repo_url = f"https://github.com/{repo}"

    if event_type == "PushEvent":
        commits = len(event["payload"]["commits"])
        print(f"[{formatted_date}] Pushed {commits} commits to {repo} ({repo_url})")
    elif event_type == "IssuesEvent":
        action = event["payload"]["action"]
        print(f"[{formatted_date}] {action.capitalize()} an issue in {repo} ({repo_url})")
    elif event_type == "WatchEvent":
        print(f"[{formatted_date}] Starred {repo} ({repo_url})")
    else:
        print(f"[{formatted_date}] {event_type} in {repo} ({repo_url})")
