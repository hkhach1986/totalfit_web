from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    textbox_username_name = "email"
    textbox_password_name = "pass"
    button_keep_sign_xpath = "//body/totalfit-root[1]/totalfit-login[1]/div[1]/div[2]/div[1]/div[2]/form[1]/div[" \
                             "3]/mat-checkbox[1]/label[1]/span[1] "
    button_login_xpath = "//span[contains(text(),'SIGN IN')]"
    button_forgot_pass_xpath = "//span[contains(text(),'Forgot password?')]"
    login_page_title = "//*[contains(text(),'SIGN IN')]"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element("name", self.textbox_username_name).clear()
        self.driver.find_element("name", self.textbox_username_name).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element("name", self.textbox_password_name).clear()
        self.driver.find_element("name", self.textbox_password_name).send_keys(password)

    def checkKeepSignIn(self):
        self.driver.find_element("xpath", self.button_keep_sign_xpath).click()

    def clickLogin(self):
        wait_username = WebDriverWait(self.driver, timeout=10)
        wait_username.until(EC.presence_of_element_located((By.XPATH, self.button_login_xpath))).click()

    def forgotPass(self):
        self.driver.find_element("xpath", self.button_forgot_pass_xpath).click()

    def get_login_page_title_text(self):
        return self.driver.find_element("xpath", self.login_page_title).text
