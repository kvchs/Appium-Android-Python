from appium import webdriver
import os


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'devices'
desired_caps['platformVersion'] = '4.3'
desired_caps['appPackage'] = 'com.tal.kaoyan'
desired_caps['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'
# desired_caps['udid'] = 'XXXXXX'  真机和模拟器共同连接时必须设置此属性
desired_caps['sessionOverride'] = True
desired_caps['noReset'] = True  # 可以让应用程序按照不是初始化方式运行

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# driver.find_element_by_id('com.tal.kao:id/tv_skip').click()
driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").send_keys("username")
driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").send_keys("password")
driver.find_element_by_id("com.tal.kaoyan:id/login_login_btn").click()
driver.quit()