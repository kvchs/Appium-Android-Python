from ScriptExample.util.start_app import start_app
driver = start_app()
element = driver.find_element_by_xpath('//*[@text="Accessibility"]')
print(element)
element.click()
element2 = driver.find_element_by_android_uiautomator('new UiSelector().textContains("Node")')
element2.click()

checkbox = driver.find_elements_by_id('com.hmh.api:id/tasklist_finished')
checkbox[2].click()
print(checkbox[2].is_selected())
driver.press_keycode('4')  # 点击返回键
driver.find_element_by_android_uiautomator('new UiSelector().text("Accessibility Service")').click()
source = driver.page_source
print(source)
driver.quit()
