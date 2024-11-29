
from base.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class UserAccount(BasePage):

    URL = 'http://users.bugred.ru/user/login/index.html'

    LOGIN_FIELD_LOCATOR = (By.XPATH, '//input[@name="login"]')
    PASSWORD_FIELD_LOCATOR = (By.XPATH, '//input[@name="password"]')
    AUTH_BUTTON_LOCATOR = (By.XPATH, '//input[@type="submit"]')
    ACCOUNT_LINK = (By.XPATH, '//a[@class="dropdown-toggle"]')
    SEARCH_FIELD = (By.XPATH, '//input[@name="q"]')
    SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')
    VIEW_BUTTON = (By.LINK_TEXT, 'Посмотреть')
    USER_EMAIL = (By.XPATH, '//td[text()="Email"]/following-sibling::td')
    FIO = (By.XPATH, '//td[text()="ФИО"]/following-sibling::td')
    BIRTH_DATE = (By.XPATH, '//td[text()="Дата рождения"]/following-sibling::td')
    START_DATE = (By.XPATH, '//td[text()="Начал работать в компании"]/following-sibling::td')
    HOBBY = (By.XPATH, '//td[text()="Хобби"]/following-sibling::td')
    NAME1 = (By.XPATH, '//td[text()="имя1"]/following-sibling::td')
    SURNAME1 = (By.XPATH, '//td[text()="фамилия1"]/following-sibling::td')
    FATHERNAME1 = (By.XPATH, '//td[text()="отчество1"]/following-sibling::td')
    CAT = (By.XPATH, '//td[text()="Кошечка"]/following-sibling::td')
    DOG = (By.XPATH, '//td[text()="Собачка"]/following-sibling::td')
    PARROT = (By.XPATH, '//td[text()="Попугайчик"]/following-sibling::td')
    CAVY = (By.XPATH, '//td[text()="Морская свинка"]/following-sibling::td')
    HAMSTER = (By.XPATH, '//td[text()="Хомячок"]/following-sibling::td')
    SQUIRREL = (By.XPATH, '//td[text()="Белочка"]/following-sibling::td')
    PHONE = (By.XPATH, '//td[text()="Телефон"]/following-sibling::td')
    ADDRESS = (By.XPATH, '//td[text()="Адрес"]/following-sibling::td')
    INN = (By.XPATH, '//td[text()="ИНН"]/following-sibling::td')
    DELETE_BUTTON = (By.XPATH, '//a[text()="Удалить"]')


    def search_account(self):
        search_field = self.find(*self.SEARCH_FIELD)
        search_field.send_keys("myemail@mail.com")
        self.find(*self.SEARCH_BUTTON).click()
        self.find(*self.VIEW_BUTTON).click()


    def verify_account(self):
        email = self.find(*self.USER_EMAIL).text
        assert email == "myemail@mail.com"
        fio = self.find(*self.FIO).text
        assert fio == 'Jane', "Mismatch in the FIO field"
        birth_date = self.find(*self.BIRTH_DATE).text
        assert birth_date == '1900-01-01', "Mismatch in the birth_date field"
        start_date = self.find(*self.START_DATE).text
        assert start_date == '1930-10-07', "Mismatch in the start_date field"
        hobby = self.find(*self.HOBBY).text
        assert hobby == 'Testing', "Mismatch in the hobby field"
        name1 = self.find(*self.NAME1).text
        assert name1 == 'John', "Mismatch in the name1 field"
        surname1 = self.find(*self.SURNAME1).text
        assert surname1 == 'John', "Mismatch in the surname1 field"
        fathername1 = self.find(*self.FATHERNAME1).text
        assert fathername1 == 'John', "Mismatch in the farthername1 field"

    def delete_user(self):
        self.find(*self.SEARCH_FIELD).send_keys("myemail@mail.com")
        self.find(*self.SEARCH_BUTTON).click()
        self.find(*self.DELETE_BUTTON).click()




