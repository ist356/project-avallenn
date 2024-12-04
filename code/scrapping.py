from playwright.sync_api import Playwright, sync_playwright, expect
import time
import pandas as pd


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    url = 'https://web.archive.org/web/20230509103953/https://www.tripadvisor.com/Restaurants-g48713-Syracuse_Finger_Lakes_New_York.html'
    page.goto(url)
    content = page.content()
    page.wait_for_selector('div.VDEXx.u.Ff.K') 
    time.sleep(5)
    restaurants = page.query_selector_all('div.VDEXx.u.Ff.K')
    list = []
    for restaurant in restaurants:
        restaurant = restaurant.inner_text()
        category = page.query_selector('div.OvkNT.K.u.FGSTQ').inner_text()
        data = restaurant, category
        list.append(data)
    df = pd.DataFrame(list, columns=['restaurant', 'information'])
    df.to_csv('code/restaurants.csv', index=False)
    #print(category)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

from playwright.sync_api import Playwright, sync_playwright, expect
import time
import pandas as pd


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    url = 'https://web.archive.org/web/20230509103953/https://www.tripadvisor.com/Restaurants-g48713-Syracuse_Finger_Lakes_New_York.html'
    page.goto(url)
    content = page.content()
    page.wait_for_selector('div.RfBGI') 
    time.sleep(5)
    restaurants = page.query_selector_all('div.RfBGI')
    list = []
    for restaurant in restaurants:
        restaurant = restaurant.inner_text()
        category = page.query_selector('div.UKYQf.o').inner_text()
        data = restaurant, category
        list.append(data)
    df = pd.DataFrame(list, columns=['restaurant', 'information'])
    df.to_csv('code/restaurantsdata.csv', index=False)
    #print(category)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)