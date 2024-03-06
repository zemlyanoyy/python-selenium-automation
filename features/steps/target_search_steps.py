from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


#@given('Open Target main page')
#def open_target_main_page(context):
   # context.driver.get("https://www.target.com/")


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(10)


@then('Search results for {expected_product} are shown')
def verify_search_results_correct(context, expected_product):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert expected_product in actual_text, f"Expected word {expected_product} not in {actual_text}"
    print("Test Case Passed")

