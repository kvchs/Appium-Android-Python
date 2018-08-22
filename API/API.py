from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
'''
api：元素定位
driver.find_element_by_id('')
driver.find_element_by_xpath('')

api: 应用安装卸载
driver.install_app('/path/xx.apk')
driver.is_app_installed('package_name')
driver.remove_app('package_name.apk')

api：应用操作相关
driver.launch_app()  # 启动应用
driver.close_app()
driver.reset()   # 重置应用
driver.background_app(10)  # 把当前应用放到app后台
driver.open_notifications()   # 打开通知栏，只有Android可用

api:文件操作相关
driver.pull_file('path/filename')  # 从设备拉出文件
driver.push_file(path='', base64data='base64')  # 向设备推送文件
driver.get_screenshot_as_file('login.png')  # 截图

api:屏幕，手势操作相关
driver.lock(10)  # 锁定屏幕
driver.swipe(75, 500, 75, 0, 0.7)   # 滑动屏幕
driver.pinch(element='')  # 捏
driver.zoom(element='')   # 屏幕放大
driver.long_press_keycode(10)    # 长按
driver.press_keycode(10)  # 短按
driver.tap()      # 点击

actions = ActionChains(driver)  # 移动到具体位置
actions.move_to(element, 10, 10)
actions.perform()

perform()  # 执行手势操作
release()  # 释放操作
wait()    # 等待

from appium.webdriver.common.touch_action import TouchAction   # TouchActon： 触摸操作
action = TouchAction(driver)
action.long_press(el='', None, None, 100).release().perform()


api: 键盘操作相关
driver.hide_keyboard()  # 在ios上收起键盘
driver.keyevent(176)   # 发送键盘事件
driver.shake()       # 摇晃设备


api: 应用上下文:
a = driver.contexts  # 列出所有可用的上下文
b = driver.current_context   # 列出当前上下文
driver.switch_to.context('NATIVE_APP')  # 切换上下文
driver.app_strings()    # 应用的字符串



api: Activity 相关
activity = driver.current_activity


键盘事件
driver.keyevent(keycode=66)  # 回车键
 """Sends a keycode to the device. Android only. Possible keycodes can be
        found in http://developer.android.com/reference/android/view/KeyEvent.html.

        :Args:
         - keycode - the keycode to be sent to the device
         - metastate - meta information about the keycode being sent
        """
    

Android 屏幕滑动
driver.swipe()
width = driver.get_window_size()['width']
height = driver.get_window_size()['height']


Android 使用断言
assertEqual('.activity', driver.current_activity)

解决中文输入问题
在Appium config中增加代码
'unicodeKeyboard:'True, # 使用unicode的编码方式发送字符
'resetKeyboard': True    Unicode键盘并非虚拟键盘，在界面上不会显示出来

'''




'''
Selector Strategies
Strategy	Description
Accessibility ID	Read a unique identifier for a UI element. For XCUITest it is the element's accessibility-id attribute. For Android it is the element's content-desc attribute.
Class name	For IOS it is the full name of the XCUI element and begins with XCUIElementType. For Android it is the full name of the UIAutomator2 class (e.g.: android.widget.TextView)
ID	Native element identifier. resource-id for android; name for iOS.
Name	Name of element
XPath	Search the app XML source using xpath (not recommended, has performance issues)
Android UiAutomator	Use the UI Automator API, in particular the UiSelector class to locate elements. In Appium you send the Java code, as a string, to the server, which executes it in the application’s environment, returning the element or elements.
IOS UIAutomation	When automating an iOS application, Apple’s Instruments framework can be used to find elements


'''
'''
元素定位方式

    1. Accessibility ID
    2. Class name
    3. ID 
    4. Name （新版不支持）
    5. XPath (不建議使用，存在性能問題)
        by_xpath('//*[@class="" and @index=""]')   多个属性组合定位
    6. Android UiAutomator
    7. 相对定位：
        root_element = driver.find_element_by_id()
        root_element.find_element_by_class_name().click()
    8.Toast
        Toast是Android的一种简易提示框，不会获取焦点，无法被点击
        解决办法:
            Appium在1.6之后开始支持识别Toast内容，需要在Capablity配置如下参数：
                desired_caps['automationName'] = 'uiautomator2'
            并且安装appium-uiautomation2-driver
            
            https://www.npmjs.com/package/appium-uiautomator2-driver
            npm install appium-uiautomator2-driver
            cnpm install appium-uiautomation2-driver
            
            完成之后，我们就可以使用cnpm代替npm来安装依赖包了。
            npm install -g cnpm --registry=https://registry.npm.taobao.org
            
            appium用uiautomator2可以定位toast，用xpath，xpath=//*[contains(@text,'手机号或密码xxxx')]
    9.H5 页面元素定位（context切换）
        
    
'''






