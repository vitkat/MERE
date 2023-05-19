import time
import pytest
from pages.authorization_page import Authorization_Page
from pages.settings import url_authorization_page


@pytest.mark.smoke
@pytest.mark.regression
def test_new_ac(browser):
    """Case №-1. A test that performs the creation of a new account"""
    link = url_authorization_page
    page = Authorization_Page(browser, link)
    page.open()
    page.button_new_ac()
    time.sleep(2)
    page.input_new_email()
    time.sleep(5)
    page.input_new_pass()
    time.sleep(5)
    page.second_new_pass()
    time.sleep(5)
    # page.button_eye_first_open()
    # time.sleep(5)
    # page.button_eye_close()
    # time.sleep(3)
    # page.button_eye_two_open()
    # time.sleep(3)
    # page.button_eye_two_close()
    page.button_next()
    # # browser.save_screenshot('registr.png')


@pytest.mark.regression
def test_signin(browser):
    """Case №-2. A test that logs in to an existing account"""
    link = url_authorization_page
    page = Authorization_Page(browser, link)
    page.open()
    page.input_email()
    page.button_nextone()
    time.sleep(2)
    page.input_password()
    time.sleep(2)
    page.button_ok()
    time.sleep(2)
    # browser.save_screenshot('vhod.png')


@pytest.mark.regression
def test_button_forgot_pass(browser):
    """Case №-3. A test that checks the "Forgot password" button"""
    link = url_authorization_page
    page = Authorization_Page(browser, link)
    page.open()
    page.input_email()
    time.sleep(2)
    page.button_nextone()
    time.sleep(2)
    page.button_lose_pass()
    time.sleep(2)
    page.button_signin()
    time.sleep(2)
    browser.save_screenshot('cha.png')