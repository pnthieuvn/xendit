"""
Element Util is an wrapper of Selenium to prevent tricky issue such as: Timeout, loading
"""
import logging
import time

from core.driver_util import browser_util
from resourses import constants
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException, \
    StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import os
from PIL import Image
from io import BytesIO
from datetime import datetime


class ElementUtil:

    def __init__(self, locator):
        self.__strategies = {
            'xpath': self._find_by_xpath,
            'css': self._find_by_css_selector
        }
        self.__locator = locator
        self.__dynamic_locator = locator

    @property
    def _driver(self):
        return browser_util.get_driver()

    @property
    def _element(self):
        return self.find_element()

    def find_element(self):
        prefix, criteria = self.__parse_locator(self.__locator)
        strategy = self.__strategies[prefix]
        return strategy(criteria)

    def __by(self, prefix):
        if prefix == "class":
            return By.CLASS_NAME
        elif prefix == "css":
            return By.CSS_SELECTOR
        else:
            return prefix

    def __parse_locator(self, locator):
        if locator.startswith(('//', '(//')):
            return 'xpath', locator
        index = self.__get_locator_separator_index(locator)
        if index != -1:
            prefix = locator[:index].strip()
            if prefix in self.__strategies:
                return prefix, locator[index + 1:].lstrip()
        return 'default', locator

    def __get_locator_separator_index(self, locator):
        if '=' not in locator:
            return locator.find(':')
        if ':' not in locator:
            return locator.find('=')
        return min(locator.find('='), locator.find(':'))

    def _find_by_xpath(self, criteria):
        return WebDriverWait(self._driver, constants.SEL_TIMEOUT).until(
            ec.presence_of_element_located((By.XPATH, criteria)))

    def _find_by_css_selector(self, criteria):
        return WebDriverWait(self._driver, constants.SEL_TIMEOUT).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, criteria)))

    @property
    def text(self):
        text = self.find_element().text
        logging.info("Get text successfully " + str(self.__locator) + ". Text = " + str(text))
        return text

    def is_enabled(self):
        return self._element.is_enabled()

    def click(self):
        try:
            self.wait_for_clickable()
            self._element.click()
            logging.info("Clicked element successfully " + str(self.__locator))
        except ElementClickInterceptedException as e:
            sources = self._driver.page_source
            file = open('page-source.txt', 'w', encoding='utf-8')
            file.write(sources)
            file.close()
            raise e

    def delay(self, seconds):
        logging.info("Sleeping " + str(seconds) + " seconds")
        time.sleep(seconds)

    def send_keys(self, *value):
        self._element.send_keys(value)
        logging.info("Send keys successfully " + str(self.__locator) + ". Key = " + str(value))

    def is_displayed(self, timeout=None):
        try:
            logging.info("is_displayed: %s" % self.__locator)
            return self.wait_for_visible(timeout).is_displayed()
        except (NoSuchElementException, TimeoutException, StaleElementReferenceException):
            return False
        except Exception as e:
            raise e

    def switch_to_iframe(self):
        self._driver.switch_to.frame(self.find_element())

    def switch_to_default_iframe(self):
        self._driver.switch_to.default_content()

    def move_to(self):
        actions = ActionChains(self._driver)
        actions.move_to_element(self._element).perform()

    def send_keys(self, key_value):
        if str(key_value).upper() in constants.KEYS:
            key_value = constants.KEYS[str(key_value).upper()]
        actions = ActionChains(self._driver)
        actions.send_keys(key_value).perform()

    def wait_for_visible(self, timeout=None):
        if timeout is None:
            timeout = constants.SEL_TIMEOUT
        prefix, criteria = self.__parse_locator(self.__locator)
        logging.info("Waiting for locator is visible " + self.__locator)
        return WebDriverWait(self._driver, timeout).until(
            ec.visibility_of_element_located((self.__by(prefix), criteria)))

    def wait_for_invisible(self, timeout=None):
        if timeout is None:
            timeout = constants.SEL_TIMEOUT
        prefix, criteria = self.__parse_locator(self.__locator)
        logging.info("Waiting for locator is invisible " + self.__locator)
        return WebDriverWait(self._driver, timeout).until(
            ec.invisibility_of_element_located((self.__by(prefix), criteria)))

    def wait_for_clickable(self, timeout=None):
        if timeout is None:
            timeout = constants.SEL_TIMEOUT
        prefix, criteria = self.__parse_locator(self.__locator)
        return WebDriverWait(self._driver, timeout).until(
            ec.element_to_be_clickable((self.__by(prefix), criteria)))

    def capture(self):
        time.sleep(constants.SHORT_SLEEP / 1000)
        self._driver.set_window_size(1000, 1000)
        x = int(self._element.location["x"])
        y = int(self._element.location["y"])
        w = int(self._element.size["width"])
        h = int(self._element.size["height"])
        scr_img = self._driver.get_screenshot_as_png()
        scr_img = Image.open(BytesIO(scr_img))
        scr_img = scr_img.crop((x * 2.5, y + x / 3.2, x * 3.85 + w, y + h / 3.7))

        now_date = datetime.now()
        if not os.path.exists(constants.TEMP_DIR):
            os.makedirs(constants.TEMP_DIR)
        image_path = constants.TEMP_DIR + str(now_date).replace(" ", "") + ".png"

        scr_img.save(image_path, format='PNG')
        return image_path
