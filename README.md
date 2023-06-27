# Intro
The automation-webfront repository allows to test to the webfront stage url

This projects requirements: 
- Python 
- Selenium (testing framework)
- Behave (for natural language styler)
- Allure (reporting)

# Project 
The project has 3 important parts:
1. CommonFiles folder
2. Tests folder
3. runner.py file

## CommonFiles folder
Here you'll find the CommonConfigs, CommonFunc and CommonSteps folders. 

When building a testing framework there is a lot that can be re-use for the testing all those functions, 
steps and configurations will be store here.

## Tests folder
In the tests folder we will have the files that will be run to for the testing, these re the `.feature` files. 

All `.feature` files will be written in natural language. 

Ex.
`    Given I go to the 'base_url' page
`

## runner.py file
This file for now calls the terminal command to run the test in the local environment. This command also creates a folder
for the allure report.

To be able to see the allure report in your local environment run the next command after the `runner.py` file:

`allure serve allure-results`

If you don't want to generate the report from allure you can just run the next command from the main folder:

`behave tests`