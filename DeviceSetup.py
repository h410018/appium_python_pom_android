'''
Created on Apr 13, 2020

@author: huangboyuan
'''
from appium import webdriver

class Device:
    
    driver = None
    
    def __init__(self,platformName,platformVersion,deviceName,udid,appPackage,appActivity,unicodeKeyboard,resetKeyboard,automationName):
        self.platformName = platformName
        self.platformVersion = platformVersion
        self.deviceName = deviceName
        self.udid = udid
        self.appPackage = appPackage
        self.appActivity = appActivity
        self.unicodeKeyboard = unicodeKeyboard
        self.resetKeyboard = resetKeyboard
        self.automationName = automationName
        
    def connect_to_appium_server(self):
        desired_caps = {} # dictionary set
        desired_caps['platformName'] = self.platformName
        desired_caps['platformVersion'] = self.platformVersion
        desired_caps['deviceName'] = self.deviceName
        desired_caps['udid']= self.udid
        desired_caps['appPackage']= self.appPackage
        desired_caps['appActivity']= self.appActivity
        desired_caps["unicodeKeyboard"]= self.unicodeKeyboard
        desired_caps["resetKeyboard"]= self.resetKeyboard
        desired_caps["automationName"]= self.automationName
        
        url = "http://localhost:4723/wd/hub"
        
        self.driver = webdriver.Remote(url,desired_caps)
        return self.driver