from frameworkdemo.unittest.myunit import StartEnd
from frameworkdemo.page_object.loginView import LoginView
import unittest
import logging


class TestLogin(StartEnd):
    def test_login_pass(self):
        logging.info("===test_login_pass===")
        login = LoginView(self.driver)
        login.login_action('username', 'password')

    def test_login_fail(self):
        logging.info("===test_login_fail===")
        login = LoginView(self.driver)
        login.login_action('username', 'error')


if __name__ == '__main__':
    unittest.main()