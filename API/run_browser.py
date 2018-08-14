from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '4.3',
    'deviceName': 'Customer Phone',
    'appPackage': 'com.android.browser',
    'appActivity': '.BrowserActivity'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
