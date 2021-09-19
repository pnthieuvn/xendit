import logging

from core.driver_util import browser_util


class BasePage:
    def __init__(self):
        self.driver = browser_util.get_driver()
        if self.driver is None:
            browser_util.start_driver()
            browser_util.maximize_browser()
            self.driver = browser_util.get_driver()

    def open_url(self, url):
        self.driver.get(url)
        logging.info("Open URL successfully " + url)

    def close_browser(self):
        self.driver.close_browser()
