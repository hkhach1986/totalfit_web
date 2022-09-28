import pytest

from page_objects.admin_page import Trainings
from page_objects.locations_page import Locations
from page_objects.user_page import UserWindow
from utilities.customLogger import LogGen
import time


class Test_003_User:

    logger = LogGen.loggen()
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_add_new_location(self, login, driver):
        self.logger.info("*********Verifying Login test ********")

        self.user_page = UserWindow(driver)
        self.location_page = Locations(driver)
        self.admin_page = Trainings(driver)
        self.logger.info("*********Login Successful********")
        self.logger.info("*********Verifying MM (user) button test for switch app ********")
        self.user_page.setUser()
        self.logger.info("*********Pass MM (user) button test for switch app ********")
        self.logger.info("*********Verifying switch app button test ********")
        self.user_page.setSwitchApp()
        assert self.location_page.get_locations_title_text() == "Tribe"
        self.logger.info("*********Pass switch app button test ********")
        time.sleep(5)
        self.location_page.tribe()
        self.location_page.add_new_tribe()

        # time.sleep(10)
        # self.up.setUser()
        # self.logger.info("*********Verifying logout button test ********")
        # self.up.setLogout()
        #
        # assert self.lp.get_login_page_title_text() == "SIGN IN"
        # self.logger.info("*********Pass logout button test********")
        # self.driver.close()
        # self.driver.quit()
