"""
Module containing common functions for the tests.
These functions are not test or feature specific.
"""

from selenium import webdriver

def go_to(url, browser_type=None):
    """
    Functions that will start instance for a specific browser and navigate to the specific url
    :param url: url to navigate to
    :param browser_type: the type of browser to start (Default is Firefox)
    :return: driver: browser instance
    """
    if not browser_type:
        driver = webdriver.Chrome(executable_path="/Users/valeriaargomedo/Documents/repos-vale/drivers/chromedriver")
    elif browser_type.lower() == 'chrome':
        driver = webdriver.Chrome(executable_path="/Users/valeriaargomedo/Documents/repos-vale/drivers/chromedriver")
    else:
        raise Exception("The browser type '{}' is not supported".format(browser_type))

    # clean url and go to it
    url = url.strip()
    driver.get(url)
    return driver
#=========================================================#

