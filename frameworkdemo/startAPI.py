from appium import webdriver
import os

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '4.3',
    'deviceName': 'Customer Phone',
    'app': os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\app\\API.apk',
    'sessionOverride': True,
    'noReset': True
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)