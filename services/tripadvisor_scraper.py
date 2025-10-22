from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from config.settings import TRIPADVISOR_URL, MAX_PAGES
from utils.file_handler import save_json

def scrape_tripadvisor():
    """Scrape review hotel dari TripAdvisor dan simpan ke file JSON di folder output/"""

    # Konfigurasi Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-web-security')
    options.add_argument('--disable-features=IsolateOrigins,site-per-process')
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    options.add_argument("--disable-gpu")

    # Jalankan browser
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get(TRIPADVISOR_URL)
    time.sleep(10)

    data = {}
    data["Hotel Name"] = driver.find_element(By.CSS_SELECTOR, 'h1').text.strip()
    data["reviews"] = []

    count = 0
    while count < MAX_PAGES:
        try:
            review_tags = driver.find_elements(By.CSS_SELECTOR, 'div[data-test-target="HR_CC_CARD"]')
            for review in review_tags:
                try:
                    name_tag = review.find_element(By.CSS_SELECTOR, 'span.biGQs._P.SewaP.OgHoE')
                    content_tag = review.find_element(By.CSS_SELECTOR, 'span.JguWG')
                    rating_tag = review.find_element(By.CSS_SELECTOR, 'svg[data-automation="bubbleRatingImage"] title')
                    review_date_tag = review.find_element(By.CSS_SELECTOR, 'div.biGQs._P.VImYz.AWdfh')
                    stay_date_tag = review.find_element(By.CSS_SELECTOR, 'span.biGQs._P.VImYz.xENVe')

                    data["reviews"].append({
                        "Review Name": name_tag.text.strip(),
                        "Review Content": content_tag.text.strip(),
                        "Rating": f"{rating_tag.get_attribute('textContent').strip().split()[0]}/5",
                        "Review Date": review_date_tag.text.strip().split(' wrote a review ')[-1],
                        "Date of Stay": stay_date_tag.text.strip()
                    })
                except Exception:
                    continue  # lewati review yang tidak lengkap

            # Klik tombol next
            next_button = driver.find_element(By.CSS_SELECTOR, 'a[data-smoke-attr="pagination-next-arrow"]')
            next_button.click()
            time.sleep(5)
            count += 1
        except Exception as e:
            print(f"Scraping berhenti di halaman ke-{count+1}: {e}")
            break

    driver.quit()

    # Simpan hasil ke output/
    filename = save_json(data)
    return {
        "status": "success",
        "message": f"Data berhasil disimpan ke {filename}",
        "hotel_name": data.get("Hotel Name"),
        "total_reviews": len(data.get("reviews", []))
    }
