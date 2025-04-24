import re
import pytest
from playwright.sync_api import Page, expect


# ✅ Test 1: Home page title
def test_homepage_loads(page: Page):
    page.goto("http://dev.mysoloro.com")
    expect(page).to_have_title(re.compile(r"(Soloro|Start Your Journey)", re.IGNORECASE))


# ✅ Test 2: Log in button should be visible and clickable
def test_login_button_visible_and_clickable(page: Page):
    page.goto("http://dev.mysoloro.com")
    login_button = page.get_by_role("link", name="Log in")

    expect(login_button).to_be_visible()
    expect(login_button).to_be_enabled()

    login_button.click()

    # Optional: Check redirection
    expect(page).to_have_url(re.compile(r"sign-in|login", re.IGNORECASE))

# ✅ Test 3: Explore Our Locations button should work
def test_explore_locations_button(page: Page):
    page.goto("http://dev.mysoloro.com")

    # Try to match the button more loosely
    explore_button = page.locator("text=Explore Our Locations")

    expect(explore_button).to_be_visible()
    expect(explore_button).to_be_enabled()

    explore_button.click()



# ✅ Test 4: Slider arrows (more specific selectors recommended)
def test_slider_arrows(page: Page):
    page.goto("http://dev.mysoloro.com")

    # Fallback to any button with common class or use nth selector temporarily
    arrows = page.locator("button")
    expect(arrows.nth(0)).to_be_visible()
    expect(arrows.nth(1)).to_be_visible()

    arrows.nth(0).click()
    arrows.nth(1).click()



