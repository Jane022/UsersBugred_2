from base.BaseTest import BaseTest
import os
from dotenv import load_dotenv

load_dotenv()

class TestLoginAndCreateUser(BaseTest):

    def test_login_as_manager_and_create_user(self):
        self.login_page.open_page()
        # self.login_page.fill_login_form("manager@mail.ru", "1")
        self.login_page.fill_login_form(os.getenv('MANAGER_LOGIN'), os.getenv('MANAGER_PASS'))
        self.login_page.click_submit_button()
        self.create_user_page.create_user_button_click()
        self.create_user_page.fill_create_user_form()



