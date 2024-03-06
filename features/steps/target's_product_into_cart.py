from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click at Add to cart button under the image of product')
def click_at_add_to_cart_under_image(context):
    context.driver.find_element(By.ID, "addToCartButtonOrTextIdFor88855031").click()
    sleep(6)


@when('Click at Add to cart button from right side navigation menu')
def click_at_add_to_cart_from_right_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, 'button[data-test="shippingButton"]').click()
    sleep(6)


@when('Click at Decline coverage button')
def click_at_decline_coverage_button(context):
    context.driver.find_element(By.CSS_SELECTOR, 'button[data-test="espDrawerContent-declineCoverageButton"]').click()
    sleep(6)


@then('Verify total price is shown')
def verify_total_price_is_shown(context):
    actual_text = context.driver.find_element(By.XPATH, "//*[text()='$90.27 total']").text
    assert '$90.27 total' in actual_text, f'Expected text "$90.27 total" not in {actual_text}'
    print("Test Case Passed")

