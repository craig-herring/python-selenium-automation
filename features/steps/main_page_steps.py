from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
HEADER_LINKS = (By.CSS_SELECTOR, "[id*='utilityNav']")
TARGET_CIRCLE = (By.CSS_SELECTOR, "[id*='utilityNav-circle']")
BENEFIT_CELLS = (By.CSS_SELECTOR, "[data-test='@web/slingshot-components/CellsComponent/Link']")


@given('Open Target main page')
def open_target_main(context):
    context.driver.get('https://www.Target.com/')


@when('Search for {search_word}')
def search_product(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(5)

@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()

@when('Open Target Circle page')
def click_circle_icon(context):
    context.driver.find_element(*TARGET_CIRCLE).click()
    sleep(3)

@then('Verify at least 1 link shown')
def verify_1_header_link_shown(context):
    link = context.driver.find_element(*HEADER_LINKS)
    print(link)

@then('Verify {link_amount} links shown')
def verify_all_header_links_shown(context, link_amount):
    link_amount = int(link_amount) #"6" => int 6
    links = context.driver.find_elements(*HEADER_LINKS)
    print(links)
    assert len(links) == link_amount, f'Expected {link_amount} links, but got {len(links)}'

@then('Verify that there are at least 10 benefit cells')
def verify_at_least_10_benefit_cells(context):
    links = context.driver.find_elements(*BENEFIT_CELLS)
    print(links)

