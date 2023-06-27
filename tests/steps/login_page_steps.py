from behave import given, then, when
from CommonFiles.CommonFuncs import webcommon
from CommonFiles.CommonSteps import webcommonsteps
from CommonFiles.CommonConfigs.locatorsconfig import LOGIN_PAGE_STAGE
from behave import when

@when("I type '{input_str}' into '{input_locator}' of login form")
def I_type_into_email_form(context, input_str,input_locator ):
    locator_type = LOGIN_PAGE_STAGE[input_locator]['type']
    locator_text = LOGIN_PAGE_STAGE[input_locator]['locator']
    webcommon.type_into_element(context,input_str,locator_type,locator_text)


# @when("I login with {type} account")
# def I_login_with_account(context, type):

@when("I click on the '{btn_name}' button")
def i_click_on_the_login_button(context, btn_name):
    if btn_name.lower() in ('login', 'log in'):
        login_btn_locator_type = LOGIN_PAGE_STAGE['submit_btn']['type']
        login_btn_locator_string = LOGIN_PAGE_STAGE['submit_btn']['locator']
    else:
        raise Exception("Not implemented")

    webcommon.click(context, login_btn_locator_type, login_btn_locator_string)

# @then("user should be logged in")
# def user_should_be_logged_in:
