'''
Created on Apr 14, 2020

@author: huangboyuan
'''
from DeviceSetup import Device
from PageObject.LoginPage import LoginPage
from PageObject.HomePage import HomePage
import unittest
import time


class loginTest(unittest.TestCase):
     
    driver = None
    
    def setUp(self):
        
        self.driver = Device(
            'Android',
            '6.0.1',
            'phone',
            'F5AZFG06J546',
            'com.zuvio.student',
            'com.zuvio.student.LauncherActivity',
            'true',
            'true',
            'UiAutomator2'
        ).connect_to_appium_server()
        
#         self.driver.implicitly_wait(15)

     
    def test_login_sucessfully(self):
        
        HomePage(self.driver).enter_login_page()
        
        loginPage = LoginPage(self.driver)
         
        loginPage.input_email("boyuan@zuvio.com")
         
        loginPage.input_password("123")
         
        loginPage.press_login_btn()
         
    
    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
        unittest.TestCase.tearDown(self)
        
if __name__ == '__main__':
    unittest.main()
    #     使用TestSuite可以做到有選擇地執行用例，不需要測試的case可以無需加入。TestSuite按照addTest()的先後順序執行，需要先執行的case先新增到TestSuite中。
#     suite = unittest.TestSuite()
#     suite.addTest(loginTest('login_sucessfully'))
#     suite.countTestCases()
#     #執行測試
#     runner = unittest.TextTestRunner()
#     runner.run(suite)