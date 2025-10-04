from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import datetime, os

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
options.add_argument("--log-level=3")  # hanya tampilkan error fatal
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--disable-gpu")  # kalau ada GPU error

if __name__ == "__main__":
    driver = webdriver.Chrome(options=options)  
    driver.implicitly_wait(10)
    driver.get('https://www.tripadvisor.com/Hotel_Review-g297697-d307567-Reviews-Bintang_Bali_Resort-Kuta_Kuta_District_Bali.html')
    time.sleep(10)
    name_tag = driver.find_element(By.CSS_SELECTOR, 'h1')
    data = {}
    if name_tag:
        data["Hotel Name"] = name_tag.text.strip()
        
    data['reviews'] = []
    count = 0
    while count < 5:  # Limit to first 5 pages for demo purposes
        try:
            review_tags = driver.find_elements(By.CSS_SELECTOR, 'div[data-test-target="HR_CC_CARD"]')
            for review in review_tags:
                review_name_tag = review.find_element(By.CSS_SELECTOR, 'span.biGQs._P.SewaP.OgHoE')
                review_content_tag = review.find_element(By.CSS_SELECTOR, 'span.JguWG')
                rating_title_element = review.find_element(By.CSS_SELECTOR, 'svg[data-automation="bubbleRatingImage"] title')
                rating_text = rating_title_element.get_attribute('textContent').strip()
                rating_value = rating_text.split()[0]
                
                if review_name_tag and review_content_tag:
                    data['reviews'].append({
                        "Review Name": review_name_tag.text.strip(),
                        "Review Content": review_content_tag.text.strip(),
                        "Rating": f"{rating_value}/5"
                    })
            driver.find_element(By.CSS_SELECTOR, 'a[data-smoke-attr="pagination-next-arrow"]').click()
            time.sleep(5)
            count += 1
        except Exception as e:
            print("No more 'Load More' button or error:", e)
            break

    os.makedirs("output", exist_ok=True)  # bikin folder output

    filename = f"output/tripadvisor_reviews_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
  