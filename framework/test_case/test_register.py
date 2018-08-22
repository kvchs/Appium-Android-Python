import logging
import random
import unittest

from framework.business_view.register_function import TestRegister
from framework.common.run_unit import BeforeAfter


class CheckRegister(BeforeAfter):
    def test_user_register(self):
        logging.info('======test register function=======')
        register = TestRegister(self.driver)

        register_username = 'username' + str(random.randint(1111, 9999))
        register_password = 'password' + str(random.randint(1111, 9999))
        register_email = 'eil' + str(random.randint(1111, 9999)) + '@ail.com'

        self.assertTrue(register.register_action(register_username, register_password, register_email))


if __name__ == '__main__':
    unittest.main()