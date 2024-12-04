from playwright.sync_api import Playwright, sync_playwright, expect
import time
import pandas as pd


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    url = 'https://web.archive.org/web/20240507043028/www.tripadvisor.com/Restaurants-g48713-Syracuse_Finger_Lakes_New_York.html'
    page.goto(url)
    content = page.content()
    page.wait_for_selector('div.VDEXx.u.Ff.K') 
    time.sleep(5)
    restaurants = page.query_selector_all('div.VDEXx.u.Ff.K')
    list = []
    for restaurant in restaurants:
        rest = restaurant.inner_text()
        #category is element right after restaurant name, element handle has not attribute next_sibling (using co pilot for the line below)
        category = restaurant.evaluate('(element) => element.nextElementSibling.textContent')
        data = rest, category
        list.append(data)
    df = pd.DataFrame(list, columns=['restaurant', 'information'])
    df.to_csv('code/restaurants.csv', index=False)
    #print(category)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
