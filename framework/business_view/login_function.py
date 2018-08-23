import logging
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from framework.common.common_method import CommonMethod
from framework.common.desired_caps import appium_desired


class TestLogin(CommonMethod):
    skip_button = (By.ID, 'com.tal.kaoyan:id/tv_skip')
    input_username = (By.ID, 'com.tal.kaoyan:id/login_email_edittext')
    input_password = (By.ID, 'com.tal.kaoyan:id/login_password_edittext')
    btn_login = (By.ID, 'com.tal.kaoyan:id/login_login_btn')
    btn_condition = (By.ID, 'com.tal.kaoyan:id/tv_agree')
    btn_recommend = (By.ID, 'com.tal.kaoyan:id/date_recommend_info_title')
    btn_self = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')
    login_message = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')
    btn_tool = (By.ID, 'com.tal.kaoyan:id/myapptitle_RightButton_textview')

    def login_action(self, username, password):
        time.sleep(10)
        # self.get_screenshot('start_page')
        self.find_element_uiautomator_text('我').click()
        self.find_element(*self.login_message).click()
        self.find_element(*self.input_username).clear()
        logging.info("input username ...")
        self.find_element(*self.input_username).send_keys(username)
        logging.info("input password ...")
        self.find_element(*self.input_password).send_keys(password)
        logging.info('click login button ...')
        self.find_element(*self.btn_login).click()

        logging.info('click agree button on popup ...')
        self.random_display_element(*self.btn_condition)
        self.random_display_element(*self.btn_recommend)
        logging.info('click user info button ...')
        self.find_element(*self.btn_self).click()
        try:
            logging.info('check username in personal info page')
            self.find_element(*self.login_message)
        except NoSuchElementException:
            logging.error("Login Error, Please Check ...")
        self.find_element_uiautomator_text('我').click()
        self.find_element(*self.btn_tool).click()
        logging.info("logout app ...")
        self.find_element_uiautomator_text('退出登录').click()
        try:
            self.find_element_uiautomator_text('确定').click()
            time.sleep(7)
            logging.info('close app')
            self.driver.close_app()
            return True
        except NoSuchElementException:
            logging.error('error')
            return False


if __name__ == '__main__':
    driver = appium_desired()
    verify_login = TestLogin(driver)
    verify_login.login_action('username', 'password')