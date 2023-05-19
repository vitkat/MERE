from .base_page import BasePage
from .locators import AuthorizationPageLocators
# from UI_Abra.pages.base_page import BasePage
# from UI_Abra.pages.locators import AuthorizationPageLocators


class Authorization_Page(BasePage):

    def button_new_ac(self):
        new_ac = self.browser.find_element(*AuthorizationPageLocators.BUTTON_NEW_AC)
        new_ac.click()

    def input_new_email(self):
        new_email = self.browser.find_element(*AuthorizationPageLocators.INPUT_NEW_EMAIL)
        new_email.send_keys('vkatryuk@yandex.ru')

    def input_new_pass(self):
        new_pass = self.browser.find_element(*AuthorizationPageLocators.INPUT_NEW_PASS)
        new_pass.send_keys('123456!Va')

    def second_new_pass(self):
        second_pass = self.browser.find_element(*AuthorizationPageLocators.SECOND_NEW_PASS)
        second_pass.send_keys('123456!Va')

    def button_eye_first_open(self):
        eye_open = self.browser.find_element(*AuthorizationPageLocators.EYE_FIRST_OPEN)
        eye_open.click()

    def button_eye_close(self):
        eye_close = self.browser.find_element(*AuthorizationPageLocators.EYE_FIRST_CLOSE)
        eye_close.click()

    def button_eye_two_open(self):
        eye_open = self.browser.find_element(*AuthorizationPageLocators.EYE_SECOND_OPEN)
        eye_open.click()

    def button_eye_two_close(self):
        eye_close = self.browser.find_element(*AuthorizationPageLocators.EYE_SECOND_CLOSE)
        eye_close.click()

    def button_next(self):
        next = self.browser.find_element(*AuthorizationPageLocators.BUTTON_NEXT)
        next.click()

    def input_email(self):
        email = self.browser.find_element(*AuthorizationPageLocators.INPUT_EMAIL)
        email.send_keys('vkatryuk@yandex.ru')

    def button_nextone(self):
        ne = self.browser.find_element(*AuthorizationPageLocators.BUTTON_NE)
        ne.click()

    def input_password(self):
        password = self.browser.find_element(*AuthorizationPageLocators.INPUT_PASSWORD)
        password.send_keys('123456!Va')

    def button_ok(self):
        ok = self.browser.find_element(*AuthorizationPageLocators.BUTTON_OK)
        ok.click()

    def button_lose_pass(self):
        lose = self.browser.find_element(*AuthorizationPageLocators.BUTTON_LOSE_PASS)
        lose.click()

    def button_signin(self):
        sign = self.browser.find_element(*AuthorizationPageLocators.BUTTON_SIGNIN)
        sign.click()