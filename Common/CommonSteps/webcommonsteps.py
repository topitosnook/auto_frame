from behave import given, then
from Common.CommonFuncs import webcommon
from Common.CommonConfigs import locatorsconfig


# start of steps definitions

@given("I go to the '{page}' page")
def go_to_page(context, page):
    print("Navigating to the page {}".format(page))
    webcommon.go_to(context, page)


# =========================================================#

@then("element '{component}' is visible")
def element_visibility(context, component):
    component_info = locatorsconfig.MY_ACCOUNT_LOCATORS.get(component)
    locator_type = component_info['type']
    locator_text = component_info['locator']
    current_element = webcommon.find_web_element(context, locator_type, locator_text)
    webcommon.is_element_visible(current_element)
