from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://xat.com/bentarab")
    time.sleep(4)
    page.frame_locator("iframe[name=\"box\"]").frame_locator("#appframe").locator("#textEntryEditable").click()
    page.frame_locator("iframe[name=\"box\"]").frame_locator("#appframe").locator("#textEntryEditable").fill("Hi")
    page.frame_locator("iframe[name=\"box\"]").frame_locator("#appframe").locator("#textEntryEditable").press("Enter")
    time.sleep(6)
    page.frame_locator("iframe[name=\"box\"]").frame_locator("#appframe").locator("#textEntryEditable").fill("How Are You?")
    page.frame_locator("iframe[name=\"box\"]").frame_locator("#appframe").locator("#textEntryEditable").press("Enter")
    time.sleep(5)
    page.frame_locator("iframe[name=\"box\"]").frame_locator("#appframe").locator("#textEntryEditable").fill("Good")
    page.frame_locator("iframe[name=\"box\"]").frame_locator("#appframe").locator("#textEntryEditable").press("Enter")
    time.sleep(5)
    page.frame_locator("iframe[name=\"box\"]").frame_locator("#appframe").locator("#textEntryEditable").fill("Ok")
    page.frame_locator("iframe[name=\"box\"]").frame_locator("#appframe").locator("#textEntryEditable").press("Enter")
    page.screenshot(path="screenshot.png", full_page=True)

    # ---------------------
    #context.close()
    time.sleep(604800)
    #browser.close()


with sync_playwright() as playwright:
    run(playwright)
