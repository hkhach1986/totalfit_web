class MyProfile:
    title_myProfile_xpath = "//*[contains(text(),'Profile Coach')]"

    def __init__(self, driver):
        self.driver = driver

    def get_profile_title_text(self):
        return self.driver.find_element("xpath", self.title_myProfile_xpath).text

