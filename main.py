from services.tripadvisor_scraper import scrape_tripadvisor
import json

if __name__ == "__main__":
    try:
        result = scrape_tripadvisor()
        print(json.dumps(result, indent=2, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({
            "status": "error",
            "message": str(e)
        }, indent=2, ensure_ascii=False))
