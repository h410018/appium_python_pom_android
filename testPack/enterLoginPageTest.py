'''
Created on Apr 13, 2020

@author: huangboyuan
'''

from DeviceSetup import Device
from PageObject.HomePage import HomePage

import time
import unittest


class enterLoginPageTest(unittest.TestCase):
     
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
              
     
    def test_press_login_btn(self):
              
        time.sleep(3)
         
        btn = HomePage(self.driver)
          
        btn.enter_login_page()     
    
    def test_press_register_btn(self):  
        
        time.sleep(3)
        
        btn = HomePage(self.driver)
        
        btn.enter_register_page()  
    
    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
        unittest.TestCase.tearDown(self)
        

if __name__ == '__main__':
#     unittest.main()

#     使用TestSuite可以做到有選擇地執行用例，不需要測試的case可以無需加入。TestSuite按照addTest()的先後順序執行，需要先執行的case先新增到TestSuite中。
    suite = unittest.TestSuite()
    suite.addTest(enterLoginPageTest('test_press_register_btn'))
    suite.addTest(enterLoginPageTest('test_press_register_btn'))
    #執行測試
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)         

