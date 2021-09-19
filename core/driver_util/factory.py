"""
Factory Util to support BrowserUtil:
- Initialize a single Web driver or multiple driver separated by key
- Get Web Driver
- Web Driver actions: Close All Driver, Switch Driver
"""
from core.driver_util.driver_manager import DriverManager

__driver = {}


def start_driver(name, driver_key="default"):
    driver = DriverManager().start_driver(name)
    __driver[driver_key] = driver
    Key.current = driver_key


def get_driver():
    try:
        return __driver[Key.current]
    except:
        return None


def close_all_driver():
    for key in __driver:
        __driver[key].quit()
    __driver.clear()


def switch_to_driver(driver_key="default"):
    Key.current = driver_key


class Key:
    current = "default"
