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
    
    def __init__(self,driver):
        self.driver = driver
        self.back_btn = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.ImageButton")
        self.email = self.driver.find_element_by_id("com.zuvio.student:id/email_editText")
        self.passwd = self.driver.find_element_by_id("com.zuvio.student:id/password_editText")
        self.query_account = self.driver.find_element_by_id("com.zuvio.student:id/query_account_textView")
        self.forget_password = self.driver.find_element_by_id("com.zuvio.student:id/forget_password_textView")
        self.login_btn = self.driver.find_element_by_id("com.zuvio.student:id/login_button")
    
    def back_front_page(self):
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.ImageButton")))
        self.back_bin.click()
    
    def input_email(self,email):
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.ID,"com.zuvio.student:id/email_editText")))
        self.email.clear()
        self.email.send_keys(email)  
        
    def input_password(self,password):
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.ID,"com.zuvio.student:id/password_editText")))
        self.passwd.clear()
        self.passwd.send_keys(password)
    
    def enter_query_password(self):
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.ID,"com.zuvio.student:id/query_account_textView")))
        self.query_account.click()
    
    def enter_forget_password(self):
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.ID,"com.zuvio.student:id/forget_password_textView")))
        self.forget_password.click()   
        
    def press_login_btn(self):
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.ID,"com.zuvio.student:id/login_button")))
        self.login_btn.click()            