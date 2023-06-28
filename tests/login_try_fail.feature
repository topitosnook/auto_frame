
Feature: My Account test

  Scenario: Validate visibility

    Given I go to the 'base_url' page
    Then element 'submit_btn' is visible

  Scenario: invalid visibility

    Given I go to the 'base_url' page
    Then element 'submit_btni' is visible