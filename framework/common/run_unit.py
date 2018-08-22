import unittest
from framework.common.desired_caps import appium_desired
import logging
from time import sleep


class BeforeAfter(unittest.TestCase):
    def setUp(self):
        logging.info('=====setUp Method ======')
        self.driver = appium_desired()

    def tearDown(self):
        logging.info('=====tearDown Method ======')
        sleep(5)
        self.driver.close_app()
