import yaml
import logging.config
from appium import webdriver
import os

CON_LOG = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\logs\\log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def appium_desired():
    file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\config\\desired_caps.yaml'
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.load(file)

    app_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'app', data['appName'])

    desired_caps = {
        'platformName': data['platformName'],
        'platformVersion': data['platformVersion'],
        'deviceName': data['deviceName'],
        'app': app_path,
        'automationName': data['automationName'],
        'appPackage': data['appPackage'],
        'appActivity': data['appActivity'],
        'noReset': data['noReset'],
        # 'unicodeKeyboard': data['unicodeKeyboard'],
        # 'resetKeyboard': data['resetKeyboard']
    }

    # logging.info("Start application " + data['deviceName'])

    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    driver.implicitly_wait(5)

    return driver


if __name__ == '__main__':
    appium_desired()


