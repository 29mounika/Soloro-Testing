from playwright.sync_api import sync_playwright

def test_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://dev.mysoloro.com/")
        assert "Soloro" in page.title()
        browser.close()
