import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    # Setup Chrome options
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless") # Uncomment to run in headless mode
    options.add_argument("--start-maximized")
    
    # Selenium 4.10+ has built-in Selenium Manager to handle drivers automatically
    driver = webdriver.Chrome(options=options)
    
    yield driver
    
    # Teardown
    driver.quit()
