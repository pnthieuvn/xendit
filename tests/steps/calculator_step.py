from behave import given, when, then, register_type
import parse
from tests.pages.calculator_page import CanvasCalcPage
from core.ocr_util import ocr_util

CanvasCalcPage = CanvasCalcPage()


@parse.with_pattern(r'.*')
def parse_nullable_string(text):
    return text


register_type(NullableString=parse_nullable_string)


@given('I open Calculator Canvas')
def open_calculator_page_step(context):
    CanvasCalcPage.open_calculator_page()


@when(r'I switch to iframe=fullframe')
def switch_to_iframe_fullframe(context):
    CanvasCalcPage.switch_to_fullframe()


@then(r'I switch back to default iframe')
def switch_to_default_iframe(context):
    CanvasCalcPage.switch_to_default_frame()


@when(r'I enter value into Calculator = "{key_value:NullableString}"')
def send_keys_to_canvas_calc(context, key_value):
    CanvasCalcPage.send_keys(key_value=key_value)


@then(r'I should be able to see "{expected_result:NullableString}"')
def capture_calculated_result(context, expected_result):
    screenshot_path = CanvasCalcPage.capture_calculated_result()
    actual_result = ocr_util.get_ocr_str(screenshot_path)
    assert actual_result == str(expected_result), "actual_result = " + str(actual_result) + " != " + "expected_result = " + str(expected_result)
