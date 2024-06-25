from selenium.webdriver.common.by import By

# Define a class to handle the Admin page elements and actions
class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.title = "OrangeHRM"  # Expected title of the Admin page
        # Locators for various elements on the Admin page
        self.user_management = (By.XPATH, '//span[text()="User Management"]')
        self.job = (By.XPATH, '//span[text()="Job"]')
        self.organization = (By.XPATH, '//span[text()="Organization"]')
        self.qualifications = (By.XPATH, '//span[text()="Qualifications"]')
        self.nationalities = (By.XPATH, '//span[text()="Nationalities"]')
        self.corporate_banking = (By.XPATH, '//span[text()="Corporate Banking"]')
        self.configuration = (By.XPATH, '//span[text()="Configuration"]')
        self.username = (By.XPATH, '//a[text()="Username"]')
        self.job_menu = (By.XPATH, '//a[text()="Job"]')

    # Method to check if the page title is correct or not
    def is_title_correct(self):
        return self.driver.title == self.title

    # Method to check if an element is present on the page
    def is_element_present(self, *locator):
        return len(self.driver.find_elements(*locator)) > 0

    # Method to validate the presence of all specified elements on the page
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


