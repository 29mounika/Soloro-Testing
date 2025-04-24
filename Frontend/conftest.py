# conftest.py in your Frontend test folder
import pytest
from playwright.sync_api import BrowserContext

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context(record_video_dir="videos/")
    yield context
    context.close()
