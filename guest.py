from playwright.sync_api import Playwright, sync_playwright, expect
import time

Xat = "https://xat.com/"
Chat = input("Chat Name : ")

def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto((Xat)+(Chat))
    time.sleep(4)
    page.frame_locator("iframe[name=\"box\"]").frame_locator("#appframe").locator("#textEntryEditable").fill("Ok")
    page.frame_locator("iframe[name=\"box\"]").frame_locator("#appframe").locator("#textEntryEditable").press("Enter")
    page.screenshot(path="screenshot.png", full_page=True)

    # ---------------------
    #context.close()
    time.sleep(604800)
    #browser.close()


with sync_playwright() as playwright:
    run(playwright)
