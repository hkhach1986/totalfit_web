import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from page_objects.user_page import UserWindow
from page_objects.login_page import LoginPage
from page_objects.locations_page import Locations
from page_objects.admin_page import Trainings
from utilities.readProperties import ReadConfig
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

baseUrl = ReadConfig.get_application_url()
username = ReadConfig.get_user_email()
password = ReadConfig.get_password()


@pytest.fixture()
def driver(browser):
    if browser == 'chrome':
        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "normal"
        driver = webdriver.Chrome(desired_capabilities=caps, service=Service(ChromeDriverManager().install()))
        print("launching Chrome browser............")
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        print("launching firefox browser.............")
    elif browser == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        print("launching edge browser................")
    else:
        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "normal"
        driver = webdriver.Chrome(desired_capabilities=caps, service=Service(ChromeDriverManager().install()))
        print("launching Chrome browser............")
    yield driver
    driver.quit()

# @pytest.fixture()
# def driver(browser):
#     if browser == 'chrome':
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         print("launching Chrome browser............")
#     elif browser == 'firefox':
#         driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
#         print("launching firefox browser.............")
#     elif browser == "edge":
#         driver = webdriver.Edge(EdgeChromiumDriverManager().install())
#         print("launching edge browser................")
#     else:
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         print("launching Chrome browser............")
#     yield driver
#     driver.quit()

@pytest.fixture()
def login(driver):
    driver.get(baseUrl)
    login_page = LoginPage(driver)
    login_page.setUserName(username)
    login_page.setPassword(password)
    login_page.clickLogin()

def pytest_addoption(parser):
    parser.addoption("--browser", default=["chrome"])


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


######################Pytest HTML report##############
# It is a hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'totalfit'
    config._metadata['Module Name'] = 'coach'
    config._metadata['Tester'] = 'Hayk'


# It is a hook for delete/modify environment info to HTML Report

@pytest.mark.optionalhook
def pytets_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugin", None)
