import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config_1 import config
from login_org import LoginPage
import time

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(config.URL)
    driver.maximize_window()
    time.sleep(2)
    yield driver
    time.sleep(2)
    driver.quit()

def test_admin_page_headers(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

        # Login as Admin
    login_page = LoginPage(driver)
    driver.implicitly_wait(30)
    login_page.login_form(
            username="Admin",
            password="admin123"
        )

        # Wait for Admin page to load and click on Admin tab
    admin_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Admin"]')))
    time.sleep(2)
    admin_tab.click()
    time.sleep(2)
    print(f"Page title before clicking : {driver.title}")


        # Validate the presence of "User Management"
    user_management_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]'
    time.sleep(2)
    user_management_element = wait.until(EC.visibility_of_element_located((By.XPATH, user_management_xpath)))
    time.sleep(2)
    assert user_management_element.text == "User Management", "User Management header is not present or text does not match"
    time.sleep(2)

        # Validate the presence of "Job"
    job_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]'
    time.sleep(2)
    job_element = wait.until(EC.visibility_of_element_located((By.XPATH, job_xpath)))
    time.sleep(2)
    assert job_element.text == "Job", "Job header is not present or text does not match"
    time.sleep(2)

        # Validate the presence of "Organization"
    organization_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]'
    time.sleep(2)
    organization_element = wait.until(EC.visibility_of_element_located((By.XPATH, organization_xpath)))
    time.sleep(2)
    assert organization_element.text == "Organization", "Organization header is not present or text does not match"
    time.sleep(2)

        # Validate the presence of "Qualifications"
    qualifications_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]'
    time.sleep(2)
    qualifications_element = wait.until(EC.visibility_of_element_located((By.XPATH, qualifications_xpath)))
    time.sleep(2)
    assert qualifications_element.text == "Qualifications", "Qualifications header is not present or text does not match"
    time.sleep(2)

        # Validate the presence of "Nationalities"
    nationalities_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]'
    time.sleep(2)
    nationalities_element = wait.until(EC.visibility_of_element_located((By.XPATH, nationalities_xpath)))
    time.sleep(2)
    assert nationalities_element.text == "Nationalities", "Nationalities header is not present or text does not match"
    time.sleep(2)

        # Validate the presence of "Corporate Banking"
    corporate_branding_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]'
    corporate_branding_element = wait.until(EC.visibility_of_element_located((By.XPATH, corporate_branding_xpath)))
    assert corporate_branding_element.text == "Corporate Branding", "Corporate Branding header is not present or text does not match"

        # Validate the presence of "Configuration"
    configuration_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]'
    configuration_element = wait.until(EC.visibility_of_element_located((By.XPATH, configuration_xpath)))
    assert configuration_element.text == "Configuration", "Configuration header is not present or text does not match"

    time.sleep(2)







