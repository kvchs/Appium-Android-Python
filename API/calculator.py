from appium import webdriver
import time


desired_caps = {
    'platformName': 'Android',
    'platformVersion': '4.4.2',
    'deviceName': 'Customer Phone',
    'appPackage': 'com.android.calculator2',
    'appActivity': '.Calculator'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element_by_xpath('//*[@text="1"]').click()
driver.find_element_by_xpath('//*[@text="3"]').click()
driver.find_element_by_xpath('//*[@text="5"]').click()
driver.find_element_by_xpath('//*[@text="DELETE"]').click()
driver.find_element_by_xpath('//*[@text="9"]').click()
driver.find_element_by_xpath('//*[@text="5"]').click()
driver.find_element_by_xpath('//*[@text="+"]').click()
driver.find_element_by_xpath('//*[@text="1"]').click()
driver.find_element_by_xpath('//*[@text="="]').click()
time.sleep(3)
driver.quit()