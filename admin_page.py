# from selenium.webdriver.common.by import By
#
# class AdminPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.title = "OrangeHRM"
#         self.user_management = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]')
#         self.job = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]')
#         self.organization = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]')
#         self.qualifications = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]')
#         self.nationalities = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]')
#         self.corporate_banking = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/ul/div[1]/li/a')
#         self.configuration = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/ul/div[2]/li/a')
#
#     def is_title_correct(self):
#         return self.driver.title == self.title
#
#     def is_element_present(self, *locator):
#         return len(self.driver.find_elements(*locator)) > 0
from selenium.webdriver.common.by import By

class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.title = "OrangeHRM"
        self.user_management = (By.XPATH, '//span[text()="User Management"]')
        self.job = (By.XPATH, '//span[text()="Job"]')
        self.organization = (By.XPATH, '//span[text()="Organization"]')
        self.qualifications = (By.XPATH, '//span[text()="Qualifications"]')
        self.nationalities = (By.XPATH, '//span[text()="Nationalities"]')
        self.corporate_banking = (By.XPATH, '//span[text()="Corporate Banking"]')
        self.configuration = (By.XPATH, '//span[text()="Configuration"]')
        self.username = (By.XPATH, '//a[text()="Username"]')
        self.job_menu = (By.XPATH, '//a[text()="Job"]')

    def is_title_correct(self):
        return self.driver.title == self.title

    def is_element_present(self, *locator):
        return len(self.driver.find_elements(*locator)) > 0

    def validate_elements(self):
        return {
            "User Management": self.is_element_present(*self.user_management),
            "Job": self.is_element_present(*self.job),
            "Organization": self.is_element_present(*self.organization),
            "Qualifications": self.is_element_present(*self.qualifications),
            "Nationalities": self.is_element_present(*self.nationalities),
            "Corporate Banking": self.is_element_present(*self.corporate_banking),
            "Configuration": self.is_element_present(*self.configuration),
            "Username": self.is_element_present(*self.username),
            "Job Menu": self.is_element_present(*self.job_menu)
        }

