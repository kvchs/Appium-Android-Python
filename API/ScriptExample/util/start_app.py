from appium import webdriver


def start_app():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '4.4.2',
        'deviceName': 'Customer Phone',
        'app': 'D:\\AppiumDocument\\APIDemos.apk'
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver
