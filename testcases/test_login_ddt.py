from selenium import webdriver
import pytest
from page_objects.login_page import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils
import time


class Test_002_DDT_Login:
    baseUrl = ReadConfig.get_application_url()
    path = ".//test_data/LoginData.xlsx"

    logger = LogGen.loggen()

    def test_login(self, setup):
        self.logger.info("**********Test_002_DDT_Login***********")
        self.logger.info("*********Verifying Login DDT test ********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)

        self.rows = ExcelUtils.get_row_count(self.path, 'Sheet1')
        print("Number of rows in excel:", self.rows)

        lst_status = []  ## empty list
        for r in range(2, self.rows + 1):
            self.user = ExcelUtils.read_data(self.path, 'Sheet1', r, 1)
            self.password = ExcelUtils.read_data(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.read_data(self.path, 'Sheet1', r, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Totalfit Workspace | Gym & Group Management Platform"
            # if self.exp=="Pass":


            # if act_title == exp_title:
            #     if self.exp == "Pass":
            #         self.logger.info("*****  Passed  ****")
            #         time.sleep(5)
            #         self.lp.setUser()
            #         self.lp.setLogout()
            #         lst_status.append("Pass")
            #         time.sleep(5)
            #     elif self.exp == "Fail":
            #         self.logger.info("*****  Failed  ****")
            #         lst_status.append("Fail")
            #         time.sleep(5)
            #
            # elif act_title != exp_title:
            #     if self.exp == "Pass":
            #         self.logger.info("*****  failed  ****")
            #         lst_status.append("Fail")
            #     elif self.exp == "Fail":
            #         self.logger.info("*****  Pass  ****")
            #         lst_status.append("Pass")

        self.driver.close()
        # if "Fail" not in lst_status:
        #     self.logger.info("******Login DDT test Passed *******")
        #     self.driver.close()
        #     assert True
        # else:
        #     self.logger.info("******Login DDT test Failed ****")
        #     self.driver.close()
        #     assert False
        #
        # self.logger.info("******End of Login DDT Test ******")
        # self.logger.info("****** completed TestLoginDDT ******")
