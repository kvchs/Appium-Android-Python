class BaseView(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def find_element_uiautomator_text(self, text):
        # print('new UiSelector().text(\"{0}\")'.format(text))
        return self.driver.find_element_by_android_uiautomator('new UiSelector().text(\"{0}\")'.format(text))

    def find_element_accessibility_id(self, accessibility_id):
        return self.driver.find_element_by_accessibility_id(accessibility_id)

    def find_toast_element(self, xpath_expression):
        # npm install appium-uiautomator2-driver
        return self.driver.find_element_by_xpath(xpath_expression)


