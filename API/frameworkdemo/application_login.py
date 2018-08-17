from API.frameworkdemo.capability import driver
from selenium.common.exceptions import NoSuchElementException
import time


def login():
    driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").clear()
    driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").send_keys("testappium")
    driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").clear()
    driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").send_keys("testappium")
    try:
        btn = driver.find_element_by_id("com.tal.kaoyan:id/login_login_btn")
    except NoSuchElementException:
        print("error")
    else:
        btn.click()
    print(driver.current_activity)
    print(driver.current_package)
    time.sleep(3)


try:
    driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()
except NoSuchElementException:
    print("无初始化页面")
time.sleep(3)
try:

    driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
except NoSuchElementException:
    login()
else:
    driver.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_username').click()
    driver.find_element_by_id().click()
    login()
