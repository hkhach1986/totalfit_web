import time

import pytest

from page_objects.admin_page import Trainings
from page_objects.locations_page import Locations
from page_objects.user_page import UserWindow
from page_objects.my_profile_page import MyProfile
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_002_User:

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_user_my_profile(self, driver, login):
        self.logger.info("*********Verifying Login test ********")
        self.driver = driver

        self.user_page = UserWindow(self.driver)
        self.my_profile_page = MyProfile(self.driver)

        self.logger.info("*********Login Successful********")
        self.logger.info("*********Verifying MM (user) button test ********")
        self.user_page.setUser()
        self.logger.info("*********Pass MM (user) button test ********")
        self.logger.info("*********Verifying My Profile button test ********")
        self.user_page.setMyProfile()
        assert self.my_profile_page.get_profile_title_text() == "Profile Coach"
        self.logger.info("*********Pass My Profile button test ********")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_user_switch_app_admin_logout(self, login, driver):
        self.driver = driver

        self.user_page = UserWindow(self.driver)
        self.location_page = Locations(self.driver)
        self.admin_page = Trainings(self.driver)

        self.logger.info("*********Verifying MM (user) button test for switch app ********")
        self.user_page.setUser()
        self.logger.info("*********Pass MM (user) button test for switch app ********")
        self.logger.info("*********Verifying switch app button test ********")
        self.user_page.setSwitchApp()

        assert self.location_page.get_locations_title_text() == "Tribe"
        self.logger.info("*********Pass switch app button test ********")
        self.driver.implicitly_wait(10)
        time.sleep(10)
        self.logger.info("*********Verifying switch admin button test ********")
        self.user_page.setUser()
        self.user_page.setSwitchAdmin()
        assert self.admin_page.get_title_trainings_text() == "Trainings"
        self.logger.info("*********Pass switch admin button test ********")

        # self.driver.implicitly_wait(10)
        # time.sleep(10)
        self.user_page.setUser()
        self.logger.info("*********Verifying logout button test ********")
        self.user_page.clickLogout()

    #####Random genrator
    # def random_generator(size = 8, chars = string.ascii_lowercase +string.digits):
    #     return ''.join(random.choice(chars) for x in range(size))
