import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Konfigurasi utama
TRIPADVISOR_URL = os.getenv("TRIPADVISOR_URL")
MAX_PAGES = int(os.getenv("MAX_PAGES", 5))
