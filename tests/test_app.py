import pytest
from selenium import webdriver

from locators import *


@pytest.fixture
def browser():
    browser = webdriver.Remote(
        command_executor='http://selenium-env:4444/wd/hub',
        options=webdriver.ChromeOptions()
    )
    browser.get("http://devops_flask_app:5555/")
    yield browser
    browser.quit()


class TestIndex:
    plus_id = "plus"
    minus_id = "minus"
    counter_id = "counter"

    button_plus = browser.find_element(locators.locate_by_id(plus_id))
    button_minus = browser.find_element(locators.locate_by_id(minus_id))
    counter = browser.find_element(locators.locate_by_id(counter_id))

    def test_plus(self, browser):
        self.button_plus.click()

    def test_minus(self, browser):
        self.button_minus.click()

    def test_increment(self, browser):
        counter_value = int(self.counter.text)

        self.button_plus.click()
        new_counter_value = int(self.counter.text)

        assert new_counter_value != counter_value

    def test_decrement(self, browser):
        counter_value = int(self.counter.text)

        self.button_minus.click()
        new_counter_value = int(self.counter.text)

        assert new_counter_value != counter_value
