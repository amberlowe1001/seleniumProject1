from typing import Any

from behave import given, when, then
from pip._internal.commands import search
from selenium.webdriver.common.by import By
from time import sleep
from unittest.test.test_program import RESULT

SEARCH_FIELD: tuple[Any, 'str'] = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
RESULTS = (By.XPATH, "//span[@class='a-color-state a-text-bold']")


@given('Amazon Help Page')
def open_google(context):
    context.driver.get('https://www.amazon.com/')


@when('Input {search_query} into Amazon search field')
def input_amazon_search(context, search_query, search_word=None):
    search_field = context.driver.find_element(*SEARCH_FIELD)
    search_field.send_keys(search_query)
    search.clear()
    assert isinstance(search_word, object)
    search.send_keys(search_word)
    sleep(4)


@when('Click on amazon search icon')
def click_search_amazon(context):
    context.driver.find_element(*SEARCH_ICON).click()
    # sleep(1)


@then('Product result for {result_word} are shown on Amazon')
def verify_search_result(context, result_word):
    actual_text = (context.driver.find_element(*RESULT).text, object)
    expected_text = f'{result_word}'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'


@then('Page URL has {query} in it')
def verify_url_contains_query(context, query, expected_text=None, actual_text=None, features=None):
    assert query in context.driver.current_url, f'electronics not in {context.driver.current_url}'
    # print('\n{}',f'{query}'expected_text')'
    # assert expected_text == features.text.stept.product_result_word
