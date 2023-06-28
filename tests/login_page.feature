
Feature: My Account smoke test

  Scenario: Login with valid account

    Given I go to the 'base_url_stage' page
    Then element 'submit_btn' is visible
    When I type 'valeria' into 'email_input' of login form
    And I type 'valeria' into 'password_input' of login form
    And I click on the 'submit_btn' button
#    Then user should be logged in
