import yaml
from appium import webdriver
import os

file = open('desired_caps.yaml', 'r')
data = yaml.load(file)

desired_caps = {
    'platformName': data['platformName'],
    'platformVersion': data['platformVersion'],
    'deviceName': data['deviceName'],
    'appPackage': data['appPackage'],
    'appActivity': data['appActivity'],
    'noReset': data['noReset']
}

driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)