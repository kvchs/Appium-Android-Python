from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'devices'
desired_caps['platformVersion'] = '4.3'
desired_caps['appPackage'] = 'com.tal.kaoyan'
desired_caps['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'
desired_caps['sessionOverride'] = True
desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)