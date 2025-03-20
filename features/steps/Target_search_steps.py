from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_target_main(context):
    context.driver.get('https://www.Target.com/')


@when('Search for coffee')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('coffee')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)


@then('Verify correct search results show')
def verify_search_results(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
    expected_text = 'coffee'
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'


@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert expected_result == actual_result, f'Expected {expected_result} did not match {actual_result}'


@when('Click Sign In')
def click_signin_button(context):
    context.driver.find_element(By.ID, "account-sign-in").click()
    sleep(3)


@then('Click Sign In from side navigation menu')
def click_signin_button_side(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()
    sleep(3)

@then("Verify Sign In form opened")
def verify_signin_opened(context):
    expected_result = 'Sign In form opened'
    actual_result = context.driver.find_element(By.XPATH, "//*[@class='sc-b40687e3-1 lgZeIE']").text
    assert expected_result == actual_result, f'Expected {expected_result} did not match {actual_result}'


