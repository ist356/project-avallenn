from playwright.sync_api import Playwright, sync_playwright, expect
import streamlit as st


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    url = 'https://www.tripadvisor.com/Restaurants-g48713-Syracuse_Finger_Lakes_New_York.html'
    page.goto(url)
    content = page.content()
    page.wait_for_selector('div.jhsNf.N.G')
    # create a loop so that we can get the data for all the restaurants
    elements_on_page = page.query_selector_all('div.jhsNf.N.G')
    print(elements_on_page)
    '''for element in elements_on_page:
        restaurant = element.inner_text()
        print(restaurant)
        restaurant = element.query_selector('div.VDEXx.u.Ff.K').inner_text()
        category = element.query_selector('div.OvkNT.K.u.FGSTQ').inner_text()
        print(restaurant)
        print(category)'''
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

    