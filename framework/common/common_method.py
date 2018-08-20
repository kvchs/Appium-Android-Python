from framework.base_view.base_view import BaseView
from framework.common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import os
import logging


class CommonMethod(BaseView):
    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipe_left(self):
        logging.info("swipe left ...")
        size = self.get_size()
        x1 = int(size[0] * 0.9)
        x2 = int(size[0] * 0.2)
        y1 = int(size[1] * 0.1)
        self.swipe(x1, y1, x2, y1, 1000)

    def get_time(self):
        time_format = time.strftime('%Y-%m-%d %H-%M-%S ')
        return time_format

    def get_screenshot(self, name):
        current_time = self.get_time()
        image = os.path.dirname(os.path.dirname(__file__)) + "/screenshots/" + current_time + name + '.png'
        logging.info("get screenshot {0}".format(name))
        self.driver.get_screenshot_as_file(image)


if __name__ == '__main__':
    driver = appium_desired()
    test_obj = CommonMethod(driver)
    test_obj.get_screenshot("test")
    test_obj.swipe_left()
    driver.close_app()