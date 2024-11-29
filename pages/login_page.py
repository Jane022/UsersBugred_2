import os
from base.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    URL = "http://users.bugred.ru/user/login/index.html"

    LOGIN_FIELD_LOCATOR = (By.XPATH, '//input[@name="login"]')
    PASSWORD_FIELD_LOCATOR = (By.XPATH, '//input[@name="password"]')
    AUTH_BUTTON_LOCATOR = (By.XPATH, '//input[@type="submit"]')


    def fill_login_form(self, login, password):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_FIELD_LOCATOR)).send_keys(login)
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD_LOCATOR)).send_keys(password)


    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.AUTH_BUTTON_LOCATOR)).click()