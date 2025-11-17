import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

PAGE_ID = os.getenv("PAGE_ID")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

def save_json(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"📁 Saved: {filename}")

# 1. Fetch 3 latest posts
posts_url = f"https://graph.facebook.com/v24.0/{PAGE_ID}/posts?limit=3&access_token={ACCESS_TOKEN}"
posts = requests.get(posts_url).json()

# Save posts to JSON
save_json("posts.json", posts)

# 2. Loop setiap postingan → ambil komentar & simpan JSON
for post in posts.get("data", []):
    post_id = post["id"]
    print("📝 POST ID:", post_id)

    comments_url = f"https://graph.facebook.com/v24.0/{post_id}/comments?access_token={ACCESS_TOKEN}"
    comments = requests.get(comments_url).json()

    # Save comments to JSON per post
    filename = f"comments_{post_id.replace('/', '_')}.json"
    save_json(filename, comments)
