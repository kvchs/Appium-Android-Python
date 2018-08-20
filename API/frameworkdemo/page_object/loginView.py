from frameworkdemo.page_object.common_fun import Common
from selenium.webdriver.common.by import By
import logging
from frameworkdemo.page_object.desired_caps import appium_desired


class LoginView(Common):
    username_type = (By.ID, 'com.tal.kaoyan:id/login_email_edittext')
    password_type = (By.ID, 'com.tal.kaoyan:id/login_password_edittext')
    login_button = (By.ID, 'com.tal.kaoyan:id/login_login_btn')

    def login_action(self, username, password):
        pass
        # self.check_skip_button()
        # self.check_cancel_button()
        #
        # logging.info("login action")
        # self.find_element(self.username_type).send_keys(username)
        # self.find_element(self.password_type).send_keys(password)


if __name__ == '__main__':
    driver = appium_desired()
    l = LoginView(driver)
    l.login_action('username', 'password')

