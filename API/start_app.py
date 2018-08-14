from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '4.3',
    'deviceName': 'Customer Phone',
    'app': 'D:\\AppiumDocument\\APIDemos.apk'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
a = driver.contexts
print(a)  # ['NATIVE_APP']

width = driver.get_window_size()['width']
height = driver.get_window_size()['height']
print(width, height)
