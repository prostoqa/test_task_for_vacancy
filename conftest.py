import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(options=options, service=service)
    yield driver
    driver.quit()
