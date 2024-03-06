from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


five_benefits = (By.CSS_SELECTOR, "[class*='styles__BenefitTextContainer']")


@given('Open Target Circle page')
def open_circle_page(context):
   context.driver.get("https://www.target.com/circle")


@when('Search the benefit boxes')
def search_benefit_boxes(context):
   context.driver.find_elements(*five_benefits)


@then('Verify 5 benefit boxes are shown')
def verify_5_benefit_boxes(context):
   actual_result = context.driver.find_elements(*five_benefits)
   assert len(actual_result) == 5, f'Expected amount of benefit boxes are not in {actual_result}'
   print("Test Case Passed")