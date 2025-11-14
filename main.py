from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import os
from datetime import datetime, timedelta
import re

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
    driver.get("https://www.traveloka.com/en-id/hotel/detail?spec=10-12-2025.11-12-2025.1.1.HOTEL.9000005505655.Sans%20Stay%20Skyland%20Pasteur%20Bandung.2&contexts=%7B%22sourceHotelDetail%22%3A%22MERCHANDISING_SEARCH%22%2C%22inventoryRateKey%22%3A%22r%2F4%2FIbSpsApptn70HsOVHP1%2Bi1SHhkRa3idkrzICNj4dEvvW%2BsMTfF0LL0XINC9JmX%2B5ad9im%2B3sPmBF6cprF%2FsiEbiy2n3yBgneU5TLRjIa7aLchboS7wdNkBRjAqgQL8Wgf%2Fmzqcmw3PrdUN%2BC4uT3cmC%2BBzZqbR8W%2FZADv0rcLzwFIvhl3NGqhf0y7SOqsZM9t9FJgBT9OWDM1zAO%2Fadzv6vbQ0LZet7Ooded%2FYodZQ%2Bmo27xejTh5Oc4izw39PCWSVDKwnP%2FUeFnHAmHq0P1a2C211JkQoCvOnw%2FXAF26T8o790RIclYDsF7jT9%2BcrFY9oFTmI%2BuhAf1m4i0MatOeW5NY22IOEmxB6kGUZmYQBC9IydWggD2lky1Dxl7zmhmrt2HpjZxmWTAoLgqttomDoUuMEjk0Bs8ifzfPptBpm91DpTdLg%2B%2FzK6QY%2FIKphJO68a4V%2F54OudS0GfgV5hAEL0jJ1aCAPaWTLUPGXvN839VozZISQisuzAFDyv%2BmukY4Wfv%2BkFduc7hBHb6pnn4aNKOyoG7Jito5SHkdjo0bXHRx6PwFsBDwx4PdDdUfTttQXVTLpoSidS2Vk2IQKraL3%2B5e1oeju2nE%2FCHues5I1GzKTMKA%2FGw3X0qzb2HoyYXRBM4iOF5d4kSWB5OPbBzIrtUW2aHE8zK5KoHXUMNq3Irs076GCmA%2BP4YD6oXbcSJ6oZJLCet0UnT8yC27MXx9mylKUoxLgOp0XlKcJ5L38183R63rhaSANgQmLS9GZIgm0f1Kzvvl64AC9qLQjyl92baEhjH7KXu%2F3LFvO%2F3dv%2FkwPzSsTcTk1CgwIzbvRNEIEtmty7rlg03z8P32UkgIWSEJpv52Ku17YIcqzYuLTydZdp%2FvNiKJYG0T1vh5YhEEUaJ0gjaG9UhELegF9iDfvpFYeWyPmUOhd4xgGidL4WrNcrtEcU06YrRzKKBnEkiDBPNSOkLn9CtqHcuDN07jrmWEhaGRurlsJdGqb1dTHaoJ%2BaCInbOunnEdLgHKtvBtAU1Ttl6NjxThdZuFPf9WT96ohkkWCZyyvBLEdr0VYWP7FHybuQA1JcGQy8ipN5odfyAeWtq42B3pPlbVVjGJiNZFfsmYTc%2FcUU8Ostb0PsVQnBPIPWLZghYzlqQT4%2BlKRq4hPHVKCjfPXR36f9JBcJad5G7ddv9CLYwQ%2BsSB7dsIH%2FwbdLqMBKBfEsRnPpsjkr7n%2B%2FeMOhK%2BvvTBrSuLNPSIZqlS86f58pOK4zc0fih6oU59%2FZY%2B0IDcWtSf%2FsgIQGDxSxG%2FSObkQ1%2FKWAvkyz5WFGAQGw9H%2FnPNCxy0WJBqk7YcVGv1lf6w3qg6tOyUQJdX6hRZjLTpLC1biZkvHEwusos36KtIzluXL8j3PqLznVAg47KVXJ2MBoL3Uaqjji27h4KZieWD5hfaN9ioPWPbSDvgWxPa0H6M4YWKPfSvkEHBYFYPIQDrD7aXXX4RjnoHwx4raDZYyB%2B58JWN72V8nvutG9ST6gY2QigUUDswIsD7KYm0WVPu2BCUIER0oodRpErrbiscIn96C6vafNdX7mZdeazbOC22iB3o4z4xpSMKeYkovHoZDid0qibKnblmvuwbkvX7xv%2BA0suAwkcsHZK0to0iq7vM7kaqLPG9Z3M1dO%2F6EBhlYT%2FD5R4OarSMvJHZfrqse0HowsNKtlTLtNnFUkWIdGK6ibe1%2FtBjNDiwsA59d8RQw%2BV8khH0Iu48RVcIJZbksPyyz9ImGA4A7Ckv3%2F9pM8C680ANkGoc3ZjMsHX4bpaQ5DFeyFV5jtcakWb3wTlw8Nir8N0KRTJ4VFq4ShicQGXCAjwPRekgkp6abl3V1XRMVF%2FQkir3ZOSMZ6bdcpWcR6BW9i0lw4oYsKI92B2TNFJePWMgmFiHhuhAWD6F0O3ftdJWVmJ7UbZFZkVE86LqHOjcJL3QNzDUqRGUrjBHrAehcOACSVZuwqgnXFYgMln8HqhU9XLlMkBPT3TkfUZNNQN1TNzwwXQDvOchk6kUrhVzcq%2FUHWNQulcWaGsuO%2B0Wdefg%2Bfft8jEuWh%2B0rsuaAnI3w%3D%3D%22%7D&funnel_source=Merchandising.mainAppHomePage.mainAppHomePage-V2-SSR-web-ID-LandingPage&funnel_id=C_0_ed6ca49c78b2974d0a19e83a04b12ddd535f1423_0_9a639ba504bf43c64502aa6c88b8cffe40e17009&internal_source=true")
    time.sleep(10)
    name_tag = driver.find_element(By.CSS_SELECTOR, 'h1')
    data = {}
    if name_tag:
        data["Hotel Name"] = name_tag.text.strip()

    data['reviews'] = []
    count = 0
    while count < 5:  # Limit to first 5 pages for demo purposes
        try:
            review_tags = driver.find_elements(By.CSS_SELECTOR, 'div.css-1dbjc4n.r-14lw9ot.r-h1746q.r-kdyh1x.r-d045u9.r-1udh08x.r-d23pfw')
            for review in review_tags:
                review_name_tag = review.find_element(By.CSS_SELECTOR, 'div.css-901oao.r-uh8wd5.r-ubezar.r-b88u0q.r-135wba7.r-fdjqy7')
                review_content_tag = review.find_element(By.CSS_SELECTOR, 'div.css-1dbjc4n.r-1udh08x > div.css-1dbjc4n > div.css-901oao.r-uh8wd5.r-1b43r93.r-majxgm.r-rjixqe.r-fdjqy7')
                rating_title_tag = review.find_element(By.CSS_SELECTOR, 'div[data-testid="tvat-ratingScore"]')
                review_date_tag = review.find_element(By.CSS_SELECTOR, 'div.css-901oao.r-1ud240a.r-uh8wd5.r-1b43r93.r-b88u0q.r-1cwl3u0.r-fdjqy7')
                # date_stay_tag = review.find_element(By.CSS_SELECTOR, 'span.biGQs._P.VImYz.xENVe')
                
                if review_name_tag and review_content_tag and rating_title_tag and review_date_tag:
                    
                    parts = re.sub(r'\b(?:Reviewed|ago)\b|\(s\)', '', review_date_tag.text.strip()).strip().split(' ')
                    if (len(parts) != 2) or (not parts[0].isdigit()) or (parts[1] not in ['day', 'week']):
                        continue
                    delta_args = {'day': {'days': int(parts[0])}, 'week': {'weeks': int(parts[0])}}
                    review_date = (datetime.today() - timedelta(**delta_args.get(parts[1], {}))).date().isoformat()
                    
                    data['reviews'].append({
                        "Review Name": review_name_tag.text.strip(),
                        "Review Content": review_content_tag.text.strip(),
                        "Rating": f"{rating_title_tag.text.strip()}/10",
                        "Review Date": review_date,
                        # "Date of Stay": date_stay_tag.text.strip()
                    })
            driver.find_element(By.CSS_SELECTOR, 'div[data-testid="next-page-btn"]').click()
            time.sleep(5)
            count += 1
        except Exception as e:
            print("No more 'Load More' button or error:", e)
            break

    os.makedirs("output", exist_ok=True)  # bikin folder output

    filename = f"output/traveloka_reviews_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)