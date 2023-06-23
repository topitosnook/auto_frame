import allure
from allure_commons.types import AttachmentType
import logging as logger

def before_feature(context):
    breakpoint()
def after_step(context, step):
    #TODO: add take screenshot to fail steps to add in report
    breakpoint()
    logger.info("AAAAA- AFTER ALL")
    logger.info("AAAAA- AFTER ALL")
    if step.status == 'failed':
        # take screenshot
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)
        print('------------')
        print('FAILED')

# def before_scenario(context, scenario):