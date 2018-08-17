from appium import webdriver
import selenium

desired_caps = {
    'platformName': 'Android',
    # 'platformVersion': '4.3',
    'platformVersion': '4.4.2',
    'deviceName': 'Customer Phone',
    'app': 'D:\\AppiumDocument\\APIDemos.apk'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
status = selenium.webdriver.common.utils.is_url_connectable("http://localhost:4723")
print(status)
# Only shell,startLogsBroadcast,stopLogsBroadcast commands are supported
# driver.execute_script("mobile: scroll", {'direction': "down"})
title = driver.execute_script('document.title')
print(title)