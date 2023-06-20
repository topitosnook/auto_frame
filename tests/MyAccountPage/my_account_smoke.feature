
Feature: My Account smoke test

  Scenario: Validate visibility

    Given I go to the 'base_url' page
    Then element 'login_btn' is visible

  Scenario: invalid visibility

    Given I go to the 'base_url' page
    Then element 'login_btni' is visible