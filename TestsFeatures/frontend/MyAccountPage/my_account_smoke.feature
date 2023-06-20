
Feature: My Account smoke test

  Scenario: Validate visibility

    Given I go to the 'base_url' page
    Then element 'login_btn' is visible
#    When I click 'first.test.user@supersqa.com' into username of login form
#    And I type 'testuserpassword' into password of login form
#    And I click on the 'login' button
#    Then user should be logged in
