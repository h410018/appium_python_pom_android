'''
Created on Apr 13, 2020

@author: huangboyuan

'''
# android app LoginPage

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class LoginPage:
    
    elements_loc = {}  
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)
        self.elements_loc = {
            "back_btn" : "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.ImageButton",
            "email" : 'com.zuvio.student:id/email_editText',
            "password" : 'com.zuvio.student:id/password_editText',
            "query_password" : 'com.zuvio.student:id/query_account_textView',
            "forget_password" : 'com.zuvio.student:id/forget_password_textView',
            "login_button" : 'com.zuvio.student:id/login_button'
            }
    
    def back_front_page(self):
        self.back_btn =self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,self.elements_loc["back_btn"])))
        self.back_btn.click()
        
    def input_email(self,email):
        self.email = self.wait.until(expected_conditions.presence_of_element_located((By.ID,self.elements_loc["email"])))
        self.email.clear()
        self.email.send_keys(email)  
        
    def input_password(self,password):    
        self.passwd = self.wait.until(expected_conditions.presence_of_element_located((By.ID,self.elements_loc["password"])))
        self.passwd.clear()
        self.passwd.send_keys(password)
        
    def enter_query_password(self):
        self.query_account = self.wait.until(expected_conditions.presence_of_element_located((By.ID,self.elements_loc["query_password"])))
        self.query_account.click()
        
    def enter_forget_password(self):
        self.forget_password = self.wait.until(expected_conditions.presence_of_element_located((By.ID,self.elements_loc["forget_password"])))
        self.forget_password.click() 
        
    def press_login_btn(self):
        self.login_btn = self.wait.until(expected_conditions.presence_of_element_located((By.ID,self.elements_loc["login_button"])))
        self.login_btn.click()            