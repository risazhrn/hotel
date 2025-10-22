import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
PLACE_ID = os.getenv("PLACE_ID")

BASE_URL = "https://maps.googleapis.com/maps/api/place/details/json"
