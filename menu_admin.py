from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.admin_menu_items = {
            "Admin": (By.ID, "menu_admin_viewAdminModule"),
            "PIM": (By.ID, "menu_pim_viewPimModule"),
            "Leave": (By.ID, "menu_leave_viewLeaveModule"),
            "Time": (By.ID, "menu_time_viewTimeModule"),
            "Recruitment": (By.ID, "menu_recruitment_viewRecruitmentModule"),
            "My Info": (By.ID, "menu_pim_viewMyDetails"),
            "Performance": (By.ID, "menu__Performance"),
            "Dashboard": (By.ID, "menu_dashboard_index"),
            "Directory": (By.ID, "menu_directory_viewDirectory"),
            "Maintenance": (By.ID, "menu_maintenance_purgeEmployee"),
            "Buzz": (By.ID, "menu_buzz_viewBuzz")
        }

    def verify_menu_items_displayed(self):
        for item_name, locator in self.admin_menu_items.items():
            try:
                element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
                assert element.is_displayed(), f"{item_name} menu item is not displayed"
                print(f"{item_name} menu item is displayed")
            except AssertionError as e:
                print(e)

