from behave import given, then
from CommonFiles.CommonFuncs import webcommon
from CommonFiles.CommonConfigs import locatorsconfig
from selenium import webdriver


# start of steps definitions

@given("I go to the '{page}' page")
def go_to_page(context, page):
    print("Navigating to the page {}".format(page))
    webcommon.go_to(context, page)


# =========================================================#

@then("element '{component}' is visible")
def element_visibility(context, component):
    component_info = locatorsconfig.LOGIN_PAGE_STAGE.get(component)
    locator_type = component_info['type']
    locator_text = component_info['locator']
    current_element = webcommon.find_web_element(context, locator_type, locator_text)
    webcommon.is_element_visible(current_element)

# =========================================================#

