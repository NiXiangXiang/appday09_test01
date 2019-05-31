from appium import webdriver
def get_phone_driver(pac,act):
    desired_caps={}
    desired_caps['platformName'] = 'android'
    desired_caps['platfromVersion'] = '5.1'
    desired_caps['deviceName'] = 'sumxing'
    desired_caps['appPackage'] = pac
    desired_caps['appActivity'] = act
    desired_caps['automationName'] = 'Uiautomator2'

    return webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
