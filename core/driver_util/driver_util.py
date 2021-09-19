"""
Driver Util:
- Initialize Web Driver: Support Chrome, Firefox.
- Manage driver version by DriverManager
- Get Web Driver
- Web Driver actions: Close Driver
"""
from resourses import constants
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class Driver:
    def __init__(self):
        self._driver = None

    def create_driver(self, browser_name="chrome"):
        if browser_name.lower() == "chrome":
            return self.init_chrome_browser()
        elif browser_name.lower() == "firefox":
            return self.init_firefox_browser()
        else:
            raise Exception("Browser not supported. We are supported for: Chrome, Firefox")

    def get_driver(self):
        return self._driver

    def quit_driver(self):
        self._driver.quit()

    def init_chrome_browser(self):
        if constants.CHROME_VERSION is not None:
            self._driver = webdriver.Chrome(executable_path=ChromeDriverManager(constants.CHROME_VERSION).install())
        else:
            self._driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self._driver.implicitly_wait(constants.SEL_TIMEOUT)
        return self._driver

    def init_firefox_browser(self):
        if constants.FIREFOX_VERSION is not None:
            self._driver = webdriver.Firefox(executable_path=GeckoDriverManager(constants.FIREFOX_VERSION).install())
        else:
            self._driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        self._driver.implicitly_wait(constants.SEL_TIMEOUT)
        return self._driver
