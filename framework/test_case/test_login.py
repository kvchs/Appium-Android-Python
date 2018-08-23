import logging
import os
import unittest

from framework.business_view.login_function import TestLogin
from framework.common.common_method import CommonMethod
from framework.common.run_unit import BeforeAfter


class CheckLogin(BeforeAfter):
    csv_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'account.csv')

    def test_login_success(self):
        logging.info('run Test login method')
        login = TestLogin(self.driver)
        common = CommonMethod(self.driver)
        data = common.get_csv_data(self.csv_file, 1)
        result = login.login_action(data[0], data[1])
        self.assertTrue(result)

    @unittest.skip('skip test login success')
    def test_login_fail(self):
        logging.info('run Test login method')
        login = TestLogin(self.driver)
        common = CommonMethod(self.driver)
        data = common.get_csv_data(self.csv_file, 2)
        result = login.login_action(data[0], data[1])
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
