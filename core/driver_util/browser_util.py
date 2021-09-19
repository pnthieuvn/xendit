"""
Browser Util:
- Initialize a single Web driver or multiple driver separated by key
- Get Web Driver
- Web Driver actions: Close driver, pen URL, switch driver, get page source, and capture screen
"""
import logging

from core.driver_util import factory


def start_driver(name="chrome", key="default"):
    factory.start_driver(name, key)


def get_driver():
    return factory.get_driver()


def maximize_browser():
    get_driver().maximize_window()


def open_url(url):
    get_driver().get(url)
    logging.info("Open URL succesfully " + url)


def switch_to_driver(driver_key="default"):
    factory.switch_to_driver(driver_key)


def close_all_driver():
    factory.close_all_driver()


def get_page_source():
    return get_driver().page_source()


def capture():
    return get_driver().get_screenshot_as_png()
