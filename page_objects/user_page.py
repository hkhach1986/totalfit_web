from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class UserWindow:
    button_user_xpath = "//*[contains(text(), 'MM')]"
    button_myProfile_xpath = "//*[contains(text(), 'My Profile')]"
    button_switch_admin_xpath = "//*[contains(text(), ' Switch to admin ')]"
    button_switch_app_xpath = "//*[contains(text(), ' Switch to app ')]"
    button_logout_xpath = "//*[contains(text(), 'Log Out')]"


    def __init__(self, driver):
        self.driver = driver

    def setUser(self):
        wait_user = WebDriverWait(self.driver, timeout=10)
        wait_user.until(EC.element_to_be_clickable((By.XPATH, self.button_user_xpath))).click()

    def setMyProfile(self):
        wait_user = WebDriverWait(self.driver, timeout=10)
        wait_user.until(EC.element_to_be_clickable((By.XPATH, self.button_myProfile_xpath))).click()

    def setSwitchApp(self):
        wait_user = WebDriverWait(self.driver, timeout=10)
        wait_user.until(EC.element_to_be_clickable((By.XPATH, self.button_switch_app_xpath))).click()

    def setSwitchAdmin(self):
        wait_user = WebDriverWait(self.driver, timeout=10)
        wait_user.until(EC.element_to_be_clickable((By.XPATH, self.button_switch_admin_xpath))).click()

    def clickLogout(self):
        wait_user = WebDriverWait(self.driver, timeout=10)
        wait_user.until(EC.element_to_be_clickable((By.XPATH, self.button_logout_xpath))).click()


