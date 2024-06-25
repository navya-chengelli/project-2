import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config_1 import config
from login_org import LoginPage
from admin_page import AdminPage

# @pytest.fixture(scope="module")
# def setup():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.get(config.URL)
#     driver.maximize_window()
#     yield driver
#     driver.quit()
#
# def test_admin_page_headers(setup):
#     driver = setup
#     wait = WebDriverWait(driver, 10)
import pytest
from selenium import webdriver
from login_org import LoginPage
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # or another browser driver
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # Replace with your login page URL
    yield driver
    time.sleep(10)
    driver.quit()

def test_login_form(driver):
    driver.implicitly_wait(30)
    login_page = LoginPage(driver)
    login_page.login_form(
        username="Admin",
        password="admin123"
    )
    #
    # def test_admin_page_headers(setup):
    #     driver = setup
    #     # wait = WebDriverWait(driver, 10)
    # # Wait for Admin page to load
    # admin_tab = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Admin"]')))
    # admin_tab.click()
    #
    # # Create an instance of AdminPage
    # admin_page = AdminPage(driver)
    #
    # #Validate the title of the page
    # assert admin_page.is_title_correct(), "The page title is incorrect"
    #
    # # Validate the presence of the specified headers
    # assert admin_page.is_element_present(*admin_page.user_management), "User Management header is not present"
    # assert admin_page.is_element_present(*admin_page.job), "Job header is not present"
    # assert admin_page.is_element_present(*admin_page.organization), "Organization header is not present"
    # assert admin_page.is_element_present(*admin_page.qualifications), "Qualifications header is not present"
    # assert admin_page.is_element_present(*admin_page.nationalities), "Nationalities header is not present"
    # assert admin_page.is_element_present(*admin_page.corporate_banking), "Corporate Banking header is not present"
    # assert admin_page.is_element_present(*admin_page.configuration), "Configuration header is not present"
