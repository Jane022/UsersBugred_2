from base.BaseTest import BaseTest
import os
from dotenv import load_dotenv

load_dotenv()

class TestUserSearchAndVerify(BaseTest):

    def test_user_search_and_verify(self):
        self.login_page.open_page()
        self.login_page.fill_login_form(os.getenv('MANAGER_LOGIN'), os.getenv('MANAGER_PASS'))
        self.login_page.click_submit_button()
        self.user_account_page.search_account()
        self.user_account_page.verify_account()



