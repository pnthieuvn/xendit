"""
Behave Hooks - Setup & Teardown
@author by Phat Le on Aug 13, 2021
"""
from behave.log_capture import capture
import allure
from behave.model_core import Status
from core.driver_util import browser_util
import logging
from pathlib import Path
from shutil import rmtree
from resourses import constants


@capture
def before_all(context):
    pass

def after_all(context):
    browser_util.close_all_driver()


def before_feature(context, feature):
    logging.info("---------------------Start Feature------------------------")
    logging.info(">>>>>> Feature: " + feature.name)


def after_feature(context, feature):
    logging.info("---------------------End Feature------------------------")
    clear_temp_flag = context.config.userdata.get('clear_temp')
    if clear_temp_flag == True or clear_temp_flag == 'True' or clear_temp_flag is None:
        for path in Path(constants.TEMP_DIR).glob('**/*'):
            if path.is_file():
                path.unlink()
            elif path.is_dir():
                rmtree(path)


def before_scenario(context, scenario):
    logging.info("---------------------Start Scenario------------------------")
    logging.info(scenario.name)


def after_scenario(context, scenario):
    logging.info("---------------------End Scenario------------------------")


def before_step(context, step):
    logging.info(step.name)


def after_step(context, step):
    step_status = step.status
    if step_status == Status.failed:
        logging.error('>>>>>> Test Failed <<<<<<')

    screenshot_flag = context.config.userdata.get('screenshot')
    if screenshot_flag == 'always' or screenshot_flag == 'passed':
        allure.attach(browser_util.capture(),
                      name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
    elif screenshot_flag is None or screenshot_flag == 'failed':
        if step.status == Status.failed:
            allure.attach(browser_util.capture(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
