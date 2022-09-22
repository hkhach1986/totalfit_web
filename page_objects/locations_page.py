from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Locations:
    title_locations_xpath = "//h2[contains(text(), 'Tribe')]"
    tribe_xpath = "//div[contains(text(),'Tribe')]"
    new_location_xpath = "//span[contains(text(),'Add new location')]"


    def __init__(self, driver):
        self.driver = driver

    def get_locations_title_text(self):
        wait_user = WebDriverWait(self.driver, timeout=10)
        return wait_user.until(EC.visibility_of_element_located((By.XPATH, self.title_locations_xpath))).text
        # self.driver.find_element("xpath", self.title_locations_xpath).text

    def tribe(self):
        #self.driver.find_element("xpath", self.tribe_xpath).click()
        wait_user = WebDriverWait(self.driver, timeout=10)
        wait_user.until(EC.visibility_of_element_located((By.XPATH, self.tribe_xpath))).click()

    def add_new_location(self):
        wait_user = WebDriverWait(self.driver, timeout=10)
        wait_user.until(EC.element_to_be_clickable((By.XPATH, self.new_location_xpath))).click()
