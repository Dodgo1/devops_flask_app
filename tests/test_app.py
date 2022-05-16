import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *

test_website_url = "http://devops_flask_app:5555/"

print("Connecting to webdriver")
driver = webdriver.Remote(
    command_executor='http://selenium-env:4444/wd/hub',
    options=webdriver.FirefoxOptions()
)


def test_increment():
    driver.get(test_website_url)

    counter = driver.find_element(By.ID, "counter")
    counter = int(counter.text) + 1

    button = driver.find_element(By.ID, "plus")
    button.click()

    newcounter = driver.find_element(By.ID, "counter")
    newcounter = int(newcounter.text)

    assert counter == newcounter

    print("Test 1 passed")


def test_decrement():
    driver.get(test_website_url)

    counter = driver.find_element(By.ID, "counter")
    counter = int(counter.text) - 1

    button = driver.find_element(By.ID, "minus")
    button.click()

    newcounter = driver.find_element(By.ID, "counter")
    newcounter = int(newcounter.text)

    assert counter == newcounter

    print("Test 2 passed")


def test_form():
    driver.get(test_website_url)

    login_input_id = "login"
    password_input_id = "password"
    button_submit_id = "submit"

    login_input = driver.find_element(*locators.locate_by_id(login_input_id))
    login_input.send_keys("test-login")

    password_input = driver.find_element(*locators.locate_by_id(password_input_id))
    password_input.send_keys("test-passwd")

    driver.find_element(*locators.locate_by_id(button_submit_id)).click()

    site_title = driver.title

    assert "Flask" in site_title


try:
    print("Test 1")
    test_increment()

    print("Test 2")
    test_decrement()

finally:
    print("Tests finished")

    driver.quit()
