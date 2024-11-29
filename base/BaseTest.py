import pytest
from pages.create_user_page import CreateUser
from pages.users_page import UserAccount
from pages.login_page import LoginPage
# from config.data import Data

class BaseTest:

    # data: Data

    login_page: LoginPage
    create_user_page: CreateUser
    user_account_page: UserAccount



    @pytest.fixture(autouse=True)
    def setup (self, request, driver):
        request.cls.driver = driver
        # request.cls.data = Data
        request.cls.login_page = LoginPage(driver)
        request.cls.create_user_page = CreateUser(driver)
        request.cls.user_account_page = UserAccount(driver)
