from frameworkdemo.page_object.baseView import BaseView
from frameworkdemo.page_object.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging


class Common(BaseView):
    cancel_button_locator = (By.ID, 'android:id/button2')
    skip_button = (By.ID, 'com.tal.kaoyan:id/tv_skip')
    
    def check_cancel_button(self):
        logging.info('============check cancel button=================')
        try:
            cancel_button = self.find_element(self.cancel_button_locator)
        except NoSuchElementException:
            logging.info("No cancel button")
        else:
            cancel_button.click()
    
    def check_skip_button(self):
        logging.info("============check skip button=================")
        try:
            skip_button = self.find_element(self.skip_button)
        except NoSuchElementException:
            logging.info('No skip button')
        else:
            skip_button.click()


if __name__ == '__main__':
    driver = appium_desired()
    com = Common(driver)
    com.check_cancel_button()
    com.check_skip_button()