from selenium.webdriver.common.keys import Keys

SEL_TIMEOUT = 5000
SHORT_SLEEP = 1000
MEDIUM_SLEEP = 2000
LONG_SLEEP = 3000
CHROME_VERSION = None
FIREFOX_VERSION = None
URL = {
    "calculator_url": "https://www.online-calculator.com/full-screen-calculator/"
}
KEYS = {
    "KEYS.NUMPAD0": Keys.NUMPAD0,
    "KEYS.NUMPAD1": Keys.NUMPAD1,
    "KEYS.NUMPAD2": Keys.NUMPAD2,
    "KEYS.NUMPAD3": Keys.NUMPAD3,
    "KEYS.NUMPAD4": Keys.NUMPAD4,
    "KEYS.NUMPAD5": Keys.NUMPAD5,
    "KEYS.NUMPAD6": Keys.NUMPAD6,
    "KEYS.NUMPAD7": Keys.NUMPAD7,
    "KEYS.NUMPAD8": Keys.NUMPAD8,
    "KEYS.NUMPAD9": Keys.NUMPAD9,
    "KEYS.ENTER": Keys.ENTER,
    "KEYS.EQUALS": Keys.EQUALS,
    "KEYS.ADD": Keys.ADD,
    "KEYS.SUBTRACT": Keys.SUBTRACT,
    "KEYS.DIVIDE": Keys.DIVIDE,
    "KEYS.PERCENTAGE": Keys.SHIFT
}

TEMP_DIR = './temp/'
