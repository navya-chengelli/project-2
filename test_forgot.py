from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class OrangeHRM:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        self.driver.get(self.url)
        sleep(3)  # Wait for 3 seconds to load page completely
        self.driver.maximize_window()

    def quit(self):
        """
        Quit the WebDriver instance.
        """
        self.driver.quit()

    def forgot_password(self):
        self.boot()  # Start the application and maximize window
        sleep(3)  # Wait for 3 seconds
        
        # Set implicit wait to 60 seconds 
        self.driver.implicitly_wait(60)

        # Click on the 'Forgot your password?' link
        forgot_password_link = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p')
        forgot_password_link.click()

        sleep(2)  #wait for 2 seconds

        # Enter username ('Admin') in the input field
        enter_username = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[1]/div/div[2]/input')
        enter_username.send_keys("Admin")

        sleep(2)  

        # Click on the 'Reset Password' button
        reset_password_button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]')
        reset_password_button.click()

        sleep(1) 
        print("Reset password link sent successfully")

        sleep(3)  # Wait for 3 seconds before quit
        self.quit()  # Quit 

# Create an instance of OrangeHRM with the login URL
obj = OrangeHRM("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Execute the forgot_password method to demonstrate the 'Forgot Password'
obj.forgot_password()

