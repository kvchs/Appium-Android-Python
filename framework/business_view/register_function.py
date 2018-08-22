import logging
import random
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from framework.common.common_method import CommonMethod
from framework.common.desired_caps import appium_desired


class TestRegister(CommonMethod):
    login_message = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')
    btn_register = (By.ID, 'com.tal.kaoyan:id/login_register_text')
    input_register_username = (By.ID, 'com.tal.kaoyan:id/activity_register_username_edittext')
    input_register_password = (By.ID, 'com.tal.kaoyan:id/activity_register_password_edittext')
    input_register_email = (By.ID, 'com.tal.kaoyan:id/activity_register_email_edittext')

    def register_action(self, register_username, register_password, register_email):
        logging.info('register with: ' + register_username)
        time.sleep(5)
        self.find_element_uiautomator_text('我').click()
        self.find_element(*self.login_message).click()
        logging.info("click register button ...")
        self.find_element(*self.btn_register).click()
        self.find_element(*self.input_register_username).clear()
        self.find_element(*self.input_register_username).send_keys(register_username)
        self.find_element(*self.input_register_password).send_keys(register_password)
        self.find_element(*self.input_register_email).send_keys(register_email)
        logging.info("click register button after input correct data")
        self.find_element_uiautomator_text('立即注册').click()
        try:
            self.find_element_uiautomator_text('隐私条款')
        except NoSuchElementException:
            logging.error('注册失败')
            self.get_screenshot('register')
            return False
        else:
            logging.info('注册成功')
            return True


if __name__ == '__main__':
    register_username = 'username' + str(random.randint(1111, 9999))
    register_password = 'password' + str(random.randint(1111, 9999))
    register_email = 'email' + str(random.randint(1111, 9999)) + '@test_email.com'
    driver = appium_desired()
    register = TestRegister(driver)
    register.register_action(register_username, register_password, register_email)