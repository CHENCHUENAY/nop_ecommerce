import pytest
import logging
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
import conftest
import time
from Utilities.ReadProperties import ReadConfig
from Utilities.customLogger import LogGen

from Utilities import XLUtilities

# @pytest.mark.usefixtures("setup_teardown")
class Test_002_DDT_Login:
    BaseUrl = ReadConfig.getApplicationUrl()
    path = './TestData/LoginData.xlsx/'
    
    
    logger=LogGen.loggen()
    logger.warning('**Test_001_Login**')



    
    def test_Login_DDT(self,setup_teardown):
        self.logger.warning('**Test_002_DDT_Login**')
        self.driver=setup_teardown
        self.driver=webdriver.Chrome()
        self.driver.get(self.BaseUrl)
        self.lp=LoginPage(self.driver)
        
        self.rows = XLUtilities.getRowCount(self.path,'sheet1')
        print('no of rows in exel ')
        status_list=[]
        for row in range(2,self.rows+1):
            self.user = XLUtilities.readData(self.path,'Sheet1',row,1)
            self.password = XLUtilities.readData(self.path,'Sheet1',row,2)
            self.exp = XLUtilities.readData(self.path,'Sheet1',row,3)
            self.lp.setPassword(self.user)
            self.lp.setPassword(self.password)
            self.lp.ClickLogin()
            time.sleep(4)
            act_title=self.driver.title
            exep_title='Dashboard / nopCommerce administration'
            
            if act_title == exep_title:
                if self.exp == 'pass':
                    self.logger.info("passed")
                    self.lp.ClickLogout()
                    status_list.append('pass')
                elif self.exp == 'fail':
                    self.logger.info("failed")
                    self.lp.ClickLogout()
                    status_list.append('fail')
                    
            elif act_title != exep_title:
                if self.exp == 'pass':
                    self.logger.info("failed")
                    status_list.append('fail')
                elif self.exp == 'fail':
                    self.logger.info("passed")
                    status_list.append('pass')
        if 'fail' not in status_list:
            self.logger.info("***Login DDT is passed***")
            self.driver.quit()
            assert True
            print('DDT_TEST IS PASSED')
        else:
            self.logger.info("***Login DDT is failed***")
            self.driver.quit()
            assert False
            print('DDT_TEST IS failed')

            
            
