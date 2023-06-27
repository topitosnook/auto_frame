"""
Module containing common functions for the tests.
These functions are not test or feature specific.
"""

from selenium import webdriver
from CommonFiles.CommonConfigs import urlconfig


def go_to(context, location):
    _url = urlconfig.URLCONFIG.get(location)

    if not _url.startswith('http'):
        base_url = urlconfig.URLCONFIG.get('base_url')
        url = base_url + _url
    else:
        url = _url

    browser = context.config.userdata.get('browser')

    if not browser:
        browser = 'chrome'

    if browser.lower() == 'chrome':
        # create instance of Firefox driver the browser type is not specified
        context.driver = webdriver.Chrome()
    elif browser.lower() == 'headlesschrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        context.driver = webdriver.Chrome(options=options)
    elif browser.lower() in ('ff', 'firefox'):
        # create instance of the Chrome driver
        context.driver = webdriver.Firefox()
    else:
        raise Exception("The browser type '{}' is not supported".format(context))

    # clean url and go to it
    url = url.strip()
    context.driver.get(url)


def find_web_element(context, locator_attribute, locator_text):
    possible_locators = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name",
                         "css selector"]

    if locator_attribute not in possible_locators:
        raise Exception('The locator attribute provided is not in the approved attributes. Or the spelling and format does not match.\
                                The approved attributes are : %s ' % possible_locators)
    try:
        element = context.driver.find_element(locator_attribute, locator_text)
        return element
    except Exception as e:
        raise Exception(e)


# =========================================================#

def is_element_visible(web_element):
    if web_element.is_displayed():
        return True
    else:
        return False

def type_into_element(context_or_element, input_value, locator_att, locator_text):

    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        input_filed = context_or_element
    else:
        input_filed = context_or_element.driver.find_element(locator_att, locator_text)

    input_filed.send_keys(input_value)

def click(context_or_element, locator_att=None, locator_text=None):

    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element = context_or_element
    else:
        element = context_or_element.driver.find_element(locator_att, locator_text)

    element.click()
