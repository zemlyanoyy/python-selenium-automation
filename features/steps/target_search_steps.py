from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


#@given('Open Target main page')
#def open_target_main_page(context):
   # context.driver.get("https://www.target.com/")


@when('Search for lamp')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('lamp')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(10)


@then('Search results for lamp are shown')
def verify_search_results_correct(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert 'lamp' in actual_text, f"Expected word lamp {actual_text}"
    print("Test Case Passed")

