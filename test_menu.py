import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config_1 import config
from login_org import LoginPage
from admin_page import AdminPage
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(config.URL)
    driver.maximize_window()

    login_page = LoginPage(driver)
    driver.implicitly_wait(30)
    login_page.login_form(
        username="Admin",
        password="admin123"
    )
    # login_page.login_as_admin(config.ADMIN_USERNAME, config.ADMIN_PASSWORD)

    yield driver

    driver.quit()

def test_admin_menu_items(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)
    admin_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Admin"]')))
    time.sleep(2)
    admin_tab.click()
    time.sleep(2)
    admin_xpath='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'
    time.sleep(2)
    admin_element =wait.until(EC.visibility_of_element_located((By.XPATH,admin_xpath)))
    time.sleep(2)
    assert admin_element.text == "Admin", "Admin header is not present or text does not match"
    time.sleep(2)
    return "Admin"
    time.sleep(2)
    pim_xpath='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    time.sleep(2)
    pim_element = wait.until(EC.visibility_of_element_located((By.XPATH,pim_xpath)))
    time.sleep(2)
    assert pim_element.text== "PIM", "PIM header is not present or text does not match"
    time.sleep(2)
    leave_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a'
    time.sleep(2)
    leave_element = wait.until(EC.visibility_of_element_located((By.XPATH,leave_xpath)))
    time.sleep(2)
    assert leave_element.text == "Leave", "Leave header is not present or text does not match"
    time.sleep(2)
    Time_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a'
    time.sleep(2)
    Time_element=wait.until(EC.visibility_of_element_located((By.XPATH,Time_xpath)))
    time.sleep(2)
    assert Time_element.text== "Time", "Time header is not present or text does not match"
    time.sleep(2)
    Recruitment_xpath='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a'
    time.sleep(2)
    Recruitment_element = wait.until(EC.visibility_of_element_located((By.XPATH,Recruitment_xpath)))
    time.sleep(2)
    assert Recruitment_element.text == "Recruitment", "Recruitment header is not present or text does not match"
    time.sleep(2)
    My_Info_xpath='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a'
    time.sleep(2)
    My_Info_element = wait.until(EC.visibility_of_element_located((By.XPATH,My_Info_xpath)))
    time.sleep(2)
    assert My_Info_element.text == "My Info", "My Info header is not present or text does not match"
    print("my_Info")
    # assert My_info_element.text == "My info", "My info header is not present or text does not match"
    time.sleep(2)
    performance_xpath='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a'
    time.sleep(2)
    performance_element=wait.until(EC.visibility_of_element_located((By.XPATH,performance_xpath)))
    time.sleep(2)
    assert performance_element.text == "performance", "performance header is not present or text does not match"
    time.sleep(2)
    dashboard_xpath='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a'
    time.sleep(2)
    dashboard_element = wait.until(EC.visibility_of_element_located((By.XPATH,dashboard_xpath)))
    time.sleep(2)
    assert dashboard_element.text == "dashboard", "dashboard header is not present or text does not match"
    time.sleep(2)
    directory_xpath='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a'
    time.sleep(2)
    director_element = wait.until(EC.visibility_of_element_located((By.XPATH,directory_xpath)))
    time.sleep(2)
    assert director_element.text == "directory", "directory header is not present or text does not match"
    time.sleep(2)
    maintenance_xpath='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a'
    time.sleep(2)
    maintenance_element = wait.until(EC.visibility_of_element_located((By.XPATH,maintenance_xpath)))
    time.sleep(2)
    assert maintenance_element .text== "maintenance", "maintenance header is not present or text does not match"
    time.sleep(2)
    claim_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a'
    claim_element=wait.until(EC.visibility_of_element_located((By.XPATH,claim_xpath)))
    time.sleep(2)
    assert claim_element.text == "claim", "claim header is not present or text does not match"
    time.sleep(2)
    buzz_xpath='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a'
    time.sleep(2)
    buzz_element=wait.until(EC.visibility_of_element_located((By.XPATH,buzz_xpath)))
    time.sleep(2)
    assert buzz_element.text == "buzz", "buzz header is not present or text does not match"
    time.sleep(2)