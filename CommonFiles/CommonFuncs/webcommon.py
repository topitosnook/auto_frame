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


#
# #=========================================================#
#
# def assert_page_tittle(context,expected_title):
#     actual_title = context.driver.title
#     print("The actual title is: {}".format(actual_title))
#     print("The expected title is: {}".format(expected_title))
#
#     assert expected_title == actual_title,"The title is not as expected" \
#                                           "Expected: {}, Actual: {}".format(expected_title,actual_title)
#     print("The page title is as expected.")
#
# # =========================================================#
#
# def assert_current_url(context,expected_url):
#     current_url = context.driver.current_url
#
#     if not expected_url.startswith('http') or not expected_url.startswith('https'):
#         expected_url = 'https://' + expected_url + '/'
#
#     assert current_url == expected_url, "The current url is not as expected." \
#                                         "Actual: {}, Expected: {}".format(current_url,expected_url)
#
#     print("The page url is as expected")
#
# # =========================================================#
#
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
#
# # =========================================================#
#
# def assert_element_visible(element):
#     if not element.is_displayed():
#         raise AssertionError('The element is not displayed')
#
# # =========================================================#
#
# def type_into_element(context_or_element, input_value, locator_att, locator_text):
#     if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
#         input_field = context_or_element
#     else:
#         input_field = context_or_element.driver.find_element(locator_att, locator_text)
#
#     input_field.send_keys(input_value)
