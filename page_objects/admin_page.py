class Trainings:
    title_trainings_xpath = "//h2[contains(text(),'Trainings')]"

    def __init__(self, driver):
        self.driver = driver

    def get_title_trainings_text(self):
        return self.driver.find_element("xpath", self.title_trainings_xpath).text

    # def setUser(self):
    #     self.driver.find_element("xpath", self.button_user_xpath).click()
    #
    # def setMyProfile(self):
    #     self.driver.find_element("xpath", self.button_myProfile_xpath).click()
    #
    # def setSwitchApp(self):
    #     self.driver.find_element("xpath", self.button_switch_app_xpath).click()
    #
    # def setSwitchAdmin(self):
    #     self.driver.find_element("xpath", self.button_switch_admin_xpath).click()
    #
    # def setLogout(self):
    #     self.driver.find_element("xpath", self.button_logout_xpath).click()


