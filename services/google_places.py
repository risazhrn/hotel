import requests
from datetime import datetime
from config.settings import API_KEY, PLACE_ID, BASE_URL
from utils.file_handler import save_json

def fetch_reviews():
    """Mengambil data review dari Google Places API dan menyimpannya ke output/."""
    if not API_KEY or not PLACE_ID:
        raise ValueError("API_KEY dan PLACE_ID harus diatur di file .env")

    params = {
        'place_id': PLACE_ID,
        'fields': 'name,rating,reviews,formatted_address,user_ratings_total',
        'key': API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data['status'] != 'OK':
        return {
            "status": "error",
            "error": data['status'],
            "message": data.get('error_message', 'Unknown error')
        }

    place = data['result']

    output = {
        "export_info": {
            "exported_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "place_id": PLACE_ID,
            "source": "Google Places API"
        },
        "place_data": {
            "name": place.get("name"),
            "address": place.get("formatted_address"),
            "overall_rating": place.get("rating"),
            "total_reviews_count": place.get("user_ratings_total")
        },
        "reviews": place.get("reviews", [])
    }

    # Simpan ke folder output/
    filename = save_json(output)
    return {
        "status": "success",
        "message": f"Data berhasil disimpan ke {filename}",
        "data_preview": {
            "place_name": place.get("name"),
            "total_reviews": len(place.get("reviews", [])),
            "overall_rating": place.get("rating")
        }
    }
