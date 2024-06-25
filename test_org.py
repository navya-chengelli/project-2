import pytest
from selenium import webdriver
from login_org import LoginPage  # Assuming LoginPage class is defined in login_org module
import time

@pytest.fixture
def driver():
    # Setup WebDriver instance
    driver = webdriver.Chrome()  # Initialize Chrome WebDriver
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # Navigate to login page URL
    yield driver  # Provide the WebDriver  to the test
    time.sleep(10)  # Wait for 10 seconds 
    driver.quit()  # Quit the browser

def test_login_form(driver):
    # Test case to validate login 
    driver.implicitly_wait(30)  # Implicit wait for element
    
    login_page = LoginPage(driver)  # Instantiate LoginPage object
    login_page.login_form(  # Call login_form method 
        username="Admin",  # Provide username
        password="admin123"  # Provide password
    )
