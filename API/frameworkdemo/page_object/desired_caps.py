import yaml
import logging.config
from appium import webdriver
import os


CON_LOG = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\log\\log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def appium_desired():
    file = open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\yaml\\desired_caps.yaml', 'r')
    data = yaml.load(file)
    desired_caps = {
        'platformName': data['platformName'],
        'platformVersion': data['platformVersion'],
        'deviceName': data['deviceName'],
        'appPackage': data['appPackage'],
        'appActivity': data['appActivity'],
        'noReset': data['noReset'],
        'unicodeKeyboard': data['unicodeKeyboard'],
        'resetKeyboard': data['resetKeyboard']
    }

    logging.info("Start application " + data['deviceName'])
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)

    return driver


if __name__ == '__main__':
    appium_desired()
    # print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\log\\log.conf')

