from behave import given, then
from Common.CommonFuncs import webcommon

# start of steps definitions

@given("I go to the '{page}' page")
def i_go_to_my_account_page(context, page):
    print("ABC",)
