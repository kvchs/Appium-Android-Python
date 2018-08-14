import unittest
from appium import webdriver
import time


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.3'
desired_caps['deviceName'] = 'Customer Phone'
desired_caps['app'] = 'D:\\AppiumDocument\\APIDemos.apk'
# 解决文本框输入中文无内容显示问题
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
current = driver.current_context
print(current)
contexts = driver.contexts
# driver.switch_to.content(contexts)
print(contexts)
# driver.quit()
driver.find_elements_by_android_uiautomator('new UiSelector().clickable(true)')
# driver.find_element_by_android_uiautomator('new UiSelector().description("")')
driver.find_element_by_android_uiautomator('text("Animation")')
el = driver.find_element_by_android_uiautomator('new UiSelector().text("Animation")')

'''
el = self.driver.find_element_by_android_viewtag('a tag name')
self.assertIsNotNone(el)
els = self.driver.find_elements_by_android_viewtag('a tag name')
self.assertIsInstance(els, list)
此方法为实现

'''

# returns the application strings from the application on the device.
strings = driver.app_strings
# driver.find_element_by_accessibility_id("")

settings = driver.get_settings()
print(strings)
print(settings)
