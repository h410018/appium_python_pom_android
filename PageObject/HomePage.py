'''
Created on Apr 13, 2020

@author: huangboyuan
'''
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

class HomePage:
    
    def __init__(self,driver):
        
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)
        self.elements_loc = {
            "login_button" : 'com.zuvio.student:id/login_button',
            "register_button" : 'com.zuvio.student:id/register_button'
            }
    # Operations
    def enter_login_page(self):
        
        self.login_btn = self.wait.until(expected_conditions.presence_of_element_located((By.ID,self.elements_loc["login_button"])))
        self.login_btn.click()
        
    def enter_register_page(self):
        
        self.register_btn = self.wait.until(expected_conditions.presence_of_element_located((By.ID,self.elements_loc["register_button"])))
        self.register_btn.click()