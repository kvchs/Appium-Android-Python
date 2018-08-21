from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '4.3',
    # 'platformVersion': '4.4.2',
    'deviceName': 'Customer Phone',
    'app': 'D:\\AppiumDocument\\APIDemos.apk',
    'sessionOverride': True
    # 'noReset': True
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
print(driver.session_id)
a = driver.contexts
print(a)  # ['NATIVE_APP']

width = driver.get_window_size()['width']
height = driver.get_window_size()['height']
print(width, height)
package = driver.current_package
print(driver.is_app_installed(package))
appStrings = driver.app_strings("en", "/path/to/file")
print(appStrings)


print(driver.end_test_coverage("Intent", "/path") + "====================")
# Message: Method has not yet been implemented
# driver.shake()
# driver.lock()
# driver.start_recording_screen()
# print(driver.is_locked())
# driver.unlock()
# driver.stop_recording_screen()
# print(driver.device_time)
driver.find_element_by_android_uiautomator('new UiSelector().text("Views")').click()
e1 = driver.find_element_by_xpath("//*[@text='Animation']")
# scroll_bar = driver.find_element_by_xpath("//*[@text='ScrollBars']")
scroll_bar = driver.find_element_by_android_uiautomator('new UiSelector().text("ScrollBars")')


# actions = ActionChains(driver)
# actions.move_to(driver.find_element_by_android_uiautomator('new UiSelector().text("ScrollBars")'))
# actions.perform()


style = driver.find_element_by_xpath("//*[@text='3. Style']")

# driver.scroll(e1, scroll_bar)
scroll_bar.click()
style.click()

ele = driver.find_element_by_android_uiautomator('new UiSelector().text("Lorem ipsum dolor sit amet.")')
actions = TouchAction(driver)
actions.scroll_from_element(ele, 10, 10)
actions.scroll(10, 100)
actions.perform()




