from base.BaseTest import BaseTest
import os
from dotenv import load_dotenv

load_dotenv()

class TestLoginAsUser(BaseTest):

    def test_login_as_user(self):
        self.login_page.open_page()
        self.login_page.fill_login_form(os.getenv('USER_LOGIN'), os.getenv('USER_PASS'))
        self.login_page.click_submit_button()
