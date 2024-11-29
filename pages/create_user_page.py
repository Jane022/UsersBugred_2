import os
from selenium.webdriver.support.select import Select
from base.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CreateUser(BasePage):

    URL = "http://users.bugred.ru/user/login/index.html"


    CREATE_USER_BTN = (By.XPATH, '//a[@class="btn btn-danger"]')
    NAME_FIELD = (By.XPATH, '//input[@name="noibiz_name"]')
    EMAIL_FIELD = (By.XPATH, '//input[@name="noibiz_email"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@name="noibiz_password"]')
    AVATAR = (By.XPATH, '//input[@name="noibiz_avatar"]')
    AVATAR_PATH = f'{os.getcwd()}/AVATAR.png'
    BIRTHDATE = (By.XPATH, '//input[@name="noibiz_birthday"]')
    GENDER = (By.XPATH, '//select[@name="noibiz_gender"]')
    DATE_START = (By.XPATH, '//input[@name="noibiz_date_start"]')
    HOBBY = (By.XPATH, '//textarea[@name="noibiz_hobby"]')
    USER_NAME1 = (By.XPATH, '//input[@name="noibiz_name1"]')
    USER_SURNAME1 = (By.XPATH, '//input[@name="noibiz_surname1"]')
    USER_FATHERNAME1 = (By.XPATH, '//input[@class="form-control numberfilter"]')
    USER_CAT = (By.XPATH, '//input[@name="noibiz_cat"]')
    USER_DOG = (By.XPATH, '//input[@name="noibiz_dog"]')
    USER_PARROT = (By.XPATH, '//input[@name="noibiz_parrot"]')
    USER_CAVY = (By.XPATH, '//input[@name="noibiz_cavy"]')
    USER_HAMSTER = (By.XPATH, '//input[@name="noibiz_hamster"]')
    USER_SQUIRREL = (By.XPATH, '//input[@name="noibiz_squirrel"]')
    USER_PHONE = (By.XPATH, '//input[@name="noibiz_phone"]')
    USER_ADDRESS = (By.XPATH, '//input[@name="noibiz_adres"]')
    USER_INN = (By.XPATH, '//input[@name="noibiz_inn"]')
    SUBMIT_BUTTON = (By.XPATH, '//input[@type="submit"]')


    def create_user_button_click(self):
        button_create_user = self.find(*self.CREATE_USER_BTN)
        button_create_user.click()

    def gender_select(self):
        dropdown = Select(self.find(*self.GENDER))
        dropdown.select_by_value("f")

    def fill_create_user_form(self):
        self.find(*self.NAME_FIELD).send_keys('Jane')
        self.find(*self.EMAIL_FIELD).send_keys('myemail@mail.com')
        self.find(*self.PASSWORD_FIELD).send_keys('12345')
        self.find(*self.AVATAR).send_keys(self.AVATAR_PATH)
        self.find(*self.BIRTHDATE).send_keys('01.01.1900')
        self.find(*self.DATE_START).send_keys('07.10.1930')
        self.gender_select()
        self.find(*self.HOBBY).send_keys('Testing')
        self.find(*self.USER_NAME1).send_keys('John')
        self.find(*self.USER_SURNAME1).send_keys('John')
        self.find(*self.USER_FATHERNAME1).send_keys('John')
        self.find(*self.USER_CAT).send_keys('John')
        self.find(*self.USER_DOG).send_keys('John')
        self.find(*self.USER_PARROT).send_keys('John')
        self.find(*self.USER_CAVY).send_keys('John')
        self.find(*self.USER_HAMSTER).send_keys('John')
        self.find(*self.USER_SQUIRREL).send_keys('John')
        self.find(*self.USER_PHONE).send_keys('John')
        self.find(*self.USER_ADDRESS).send_keys('John')
        self.find(*self.USER_INN).send_keys('John')
        self.find(*self.SUBMIT_BUTTON).click()





