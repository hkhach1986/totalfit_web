from selenium import webdriver
import pytest
from page_objects.login_page import LoginPage
from page_objects.user_page import UserWindow
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Test_001_Login:
    baseUrl = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_password()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, driver):
        self.logger.info("****************Test_001_Login***********")
        self.logger.info("***********Verifying Home Page **********")
        self.driver = driver
        self.driver.get(self.baseUrl)
        actual_title = self.driver.title
        if actual_title == "Totalfit Workspace | Gym & Group Management Platform":

            self.driver.close()
            self.logger.info("*********Home Page Pass********")
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*********Home Page Fail********")
            assert False

    @pytest.mark.sanity
    def test_login(self, driver):
        self.logger.info("*********Verifying Login test ********")
        self.driver = driver
        self.driver.get(self.baseUrl)
        self.user_page = UserWindow(self.driver)
        self.login_page = LoginPage(self.driver)
        self.login_page.setUserName(self.username)
        self.login_page.setPassword(self.password)
        self.login_page.clickLogin()

        # self.driver.maximize_window()
        self.logger.info("*********Verifying set login button test ********")

        self.user_page.setUser()

        self.logger.info("*********Verifying MM button test ********")
        # time.sleep(3)

        self.user_page.clickLogout()
        self.logger.info("*********Verifying logout button test ********")

        # actual_title = self.driver.title
        #
        # if actual_title == "Totalfit Workspace | Gym & Group Management Platform":
        #     self.driver.close()
        #     self.logger.info("*********Login Home Page Pass********")
        #     assert True
        # else:
        #     self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
        #     self.driver.close()
        #     self.logger.error("*********Login Home Page Fail********")
        #     assert False
