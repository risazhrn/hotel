from services.google_places import fetch_reviews
import json

if __name__ == "__main__":
    try:
        result = fetch_reviews()
        print(json.dumps(result, indent=2, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({
            "status": "error",
            "message": str(e)
        }, indent=2, ensure_ascii=False))
