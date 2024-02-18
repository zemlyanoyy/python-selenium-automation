from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click Sign In')
def click_on_signin(context):
    context.driver.find_element(By.XPATH, "//span[@class='styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3']").click()


@when('From right side navigation menu, click Sign In')
def click_on_right_side_signin(context):
    context.driver.find_element(By.XPATH, "//span[@class='styles__ListItemText-sc-diphzn-1 jaMNVl']").click()
    sleep(6)


@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    actual_text = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    assert 'Sign into your Target account' in actual_text, f'Expected text "Sign into your Target account" not in {actual_text}'
    print("Test Case Passed")