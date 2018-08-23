import logging
import os
import time
import csv

from selenium.common.exceptions import NoSuchElementException

from framework.base_view.base_view import BaseView
from framework.common.desired_caps import appium_desired


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

    def swipe_up(self):
        logging.info('swipe up ...')
        size = self.get_size()
        x1 = int(size[0]*0.7)
        y1 = int(size[1]*0.9)
        y2 = int(size[1]*0.1)
        self.swipe(x1, y1, x1, y2, 1000)

    def get_time(self):
        time_format = time.strftime('%Y-%m-%d %H-%M-%S ')
        return time_format

    def get_screenshot(self, name):
        current_time = self.get_time()
        image = os.path.dirname(os.path.dirname(__file__)) + "/screenshots/" + current_time + name + '.png'
        logging.info("get screenshot {0}".format(name))
        self.driver.get_screenshot_as_file(image)

    def random_display_element(self, *loctor):
        try:
            element = self.find_element(*loctor)
        except NoSuchElementException:
            pass
        else:
            element.click()

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self, start_x, start_y, end_x, end_y, duration):
        # - duration - (optional) time to take the swipe, in ms.
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def get_csv_data(self, csv_file, read_line):
        logging.info('read data in csv file ==>' + csv_file)
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == read_line:
                    return row

    def element_into_view(self, *loctor):
        try:
            while not self.driver.find_element(*loctor):
                self.swipe_up()
        except NoSuchElementException:
            pass


if __name__ == '__main__':
    driver = appium_desired()
    test_obj = CommonMethod(driver)
    # test_obj.get_screenshot("test")
    # test_obj.swipe_left()
    # driver.close_app()
    csv_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'account.csv')
    print(test_obj.get_csv_data(csv_file, 2))
    print(csv_file)