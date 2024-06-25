from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# # Navigate to IMDb search page
class orange:
    def __init__(self,url):
        self.url=url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        self.driver.get(self.url)
        sleep(3)
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()
    def forgot_password(self):
        self.boot()
        sleep(3)

        self.driver.implicitly_wait(60)
        forgot_password = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p').click()

        sleep(2)
        enter_username = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[1]/div/div[2]/input')
        enter_username.send_keys("Admin")
        sleep(2)
        reset_password = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]').click()
        sleep(1)
        print("Reset password link sent sucessfully")
        sleep(3)
        self.quit()

obj = orange("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
obj.forgot_password()
