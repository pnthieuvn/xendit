from core.selenium_util.element_util import ElementUtil
from tests.pages.base_page import BasePage
from resourses import constants


class CanvasCalcPage(BasePage):
    def __init__(self):
        super().__init__()
        self.iframe_fullframe = ElementUtil("xpath=//iframe[@id='fullframe']")
        self.canvas_calc = ElementUtil("xpath=//canvas[@id='canvas']")

    def open_calculator_page(self):
        self.open_url(constants.URL["calculator_url"])

    def switch_to_fullframe(self):
        self.iframe_fullframe.switch_to_iframe()

    def switch_to_default_frame(self):
        self.iframe_fullframe.switch_to_default_iframe()

    def click_on_canvas(self):
        self.canvas_calc.click()

    def send_keys(self, key_value):
        self.canvas_calc.send_keys(key_value=key_value)

    def capture_calculated_result(self):
        return self.canvas_calc.capture()
