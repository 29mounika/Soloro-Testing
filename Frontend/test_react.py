import re
import pytest
from playwright.sync_api import expect


# ✅ Test 1: Home page title
def test_homepage_loads(context):
    page = context.new_page()
    page.goto("http://dev.mysoloro.com")
    expect(page).to_have_title(re.compile(r"(Soloro|Start Your Journey)", re.IGNORECASE))


# ✅ Test 2: Log in button should be visible and clickable
def test_login_button_visible_and_clickable(context):
    page = context.new_page()
    page.goto("http://dev.mysoloro.com")
    login_button = page.get_by_role("link", name="Log in")

    expect(login_button).to_be_visible()
    expect(login_button).to_be_enabled()

    login_button.click()
    expect(page).to_have_url(re.compile(r"sign-in|login", re.IGNORECASE))


# ✅ Test 3: Explore Our Locations button should work
def test_explore_locations_button(context):
    page = context.new_page()
    page.goto("http://dev.mysoloro.com")

    explore_button = page.locator("text=Explore Our Locations")
    expect(explore_button).to_be_visible()
    expect(explore_button).to_be_enabled()

    explore_button.click()


# ✅ Test 4: Slider arrows
def test_slider_arrows(context):
    page = context.new_page()
    page.goto("http://dev.mysoloro.com")

    arrows = page.locator("button")
    expect(arrows.nth(0)).to_be_visible()
    expect(arrows.nth(1)).to_be_visible()

    arrows.nth(0).click()
    arrows.nth(1).click()

    #################################################
    def test_page_load(page):
        page.goto("https://dev.mysoloro.com/find-clubs")
        assert page.title() != ""  # Basic check
        assert page.locator("text=Choose A Club By").is_visible()

        search_input = page.get_by_placeholder("Search Name, City Or Zip Code")
        search_input.fill("banglore")
        page.get_by_role("button", name="Search").click()

        # Expect at least one result
        page.wait_for_selector("text=Book Club", timeout=5000)
        assert page.locator("text=Book Club").is_visible()
        # Check for empty state (you may need to update selector/text based on actual app)
        assert not page.locator(".club-card").is_visible()
        input_box = page.get_by_placeholder("Search Name, City Or Zip Code")
        input_box.fill("banglore")

        # Click clear 'X' icon
        page.locator("button:has-text('×')").click()
        assert input_box.input_value() == ""


