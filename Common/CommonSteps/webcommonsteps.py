from behave import given, then
from Common.CommonFuncs import webcommon
# start of steps definitions

@given("I go to the '{page}' page")
def go_to_page(context, page):

    print("Navigating to the page {}".format(page))

    context.driver = webcommon.go_to(context, page)

#=========================================================#
