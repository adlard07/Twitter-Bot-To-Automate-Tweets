import time
from selenium import webdriver
from selenium.webdriver.common.by import By


from dataclasses import dataclass

def fetch_image_urls(query: str, max_links_to_fetch: int, wd: webdriver, sleep_between_interactions: int = 2):
    search_url = "https://www.google.com/search?sca_esv=557132508&rlz=1C1VDKB_enIN970IN970&q={search_term.replace(' ', +)}&tbm=isch&source=lnms&sa=X&ved=2ahUKEwiUu6_Ght-AAxVVGogKHa97B98Q0pQJegQICxAB&biw=1366&bih=619&dpr=1"
    wd.get(search_url.format(q=query))
    image_urls= set()
    imageCount = 0
    while imageCount < max_links_to_fetch:
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        thumbnail_results = wd.find_elements(By.CSS_SELECTOR,"img.Q4LuWd")

        for img in thumbnail_results:
            try:
                img.click()
                time.sleep(1)
            except Exception:
                continue
            actualImages = wd.find_elements(By.CSS_SELECTOR,'img.r48jcc')
            print(len(actualImages))
            for actualImage in actualImages:
                if actualImage.get_attribute('src') and 'http' in actualImage.get_attribute('src'):
                    print(actualImage.get_attribute('src'))
                    image_urls.add(actualImage.get_attribute('src'))
                    image_urls = set(image_urls)
            imageCount = len(image_urls)

            if imageCount == max_links_to_fetch:
                break

    return image_urls

@dataclass
class GetItems:
    def get_image(self):
        wd = webdriver.Chrome()
        search_term = "coding memes"
        num_images = 1000
        image_url = fetch_image_urls(search_term, num_images, wd)

        return image_url
