from appium import webdriver
import os
from appium.common.exceptions import NoSuchContextException
from selenium.common.exceptions import NoSuchElementException
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'devices'
desired_caps['platformVersion'] = '4.3'
desired_caps['appPackage'] = 'com.tal.kaoyan'
desired_caps['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'
# desired_caps['udid'] = 'XXXXXX'  真机和模拟器共同连接时必须设置此属性
desired_caps['sessionOverride'] = True
desired_caps['noReset'] = True  # 可以让应用程序按照不是初始化方式运行
# 解决中文不可见问题
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# driver.find_element_by_id('com.tal.kao:id/tv_skip').click()
driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").send_keys("自学网2018")
driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").send_keys("zxw2018")
try:
    btn = driver.find_element_by_id("com.tal.kaoyan:id/login_login_btn")
except NoSuchElementException:
    print("error")
else:
    btn.click()
print(driver.current_activity)
print(driver.current_package)
time.sleep(3)
driver.quit()