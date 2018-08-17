from appium import webdriver

desired_caps = desired_caps = {
  'platformName': 'Android',
  'platformVersion': '4.4.2',
  'deviceName': 'Android Emulator',
    # UIAutomation2 is only supported since Android 5.0 (Lollipop). You could still use other supported backends in order to automate older Android versions.
  # 'automationName': 'UiAutomator2',
  'app': 'D:\\AppiumDocument\\APIDemos.apk'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# driver.set_page_load_timeout(3)
# 设置驱动程序在搜索元素时应该等待的时间
driver.implicitly_wait(5)
# desired_cap = driver.desired_capabilities()
# print(desired_caps)



screenshotBase64 = driver.get_screenshot_as_base64()
print(screenshotBase64)

'''
(NOTE: iOS and Android don't have standard ways of defining their application source, so on calls to 'Get Page Source' Appium traverses the app hierarchy and creates an XML document. Thus, getting the source can often be an expensive and time-consuming operation)

'''

# Set the amount of time, in milliseconds, that asynchronous scripts executed by execute async are permitted to run before they are aborted (Web context only)
# driver.set_script_timeout(5000)

orientation = driver.orientation
print(orientation)

geolocation = driver.log_types
print(geolocation)

logs = driver.get_log('logcat')
print(logs)

# driver.start_activity("com.example", "ActivityName")

activity = driver.current_activity
print(activity)
package = driver.current_package
print(package)