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
        self.login_btn = self.driver.find_element_by_id("com.zuvio.student:id/login_button")
        self.register_btn = self.driver.find_element_by_id("com.zuvio.student:id/register_button")
       
    # Operations
    def enter_login_page(self):
        
        WebDriverWait(self.driver,50).until(expected_conditions.presence_of_element_located((MobileBy.ID,'com.zuvio.student:id/login_button')))
        self.login_btn.click()
        
    def enter_register_page(self):
        
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.ID,'com.zuvio.student:id/register_button')))
        self.register_btn.click()