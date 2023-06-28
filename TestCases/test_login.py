import pytest
import logging
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
import conftest
import time
from Utilities.ReadProperties import ReadConfig
from Utilities.customLogger import LogGen


# @pytest.mark.usefixtures("setup_teardown")
class Test_001_Login:
    BaseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()
    logger.warning('**Test_001_Login**')


    # @pytest.mark.usefixtures("setup_teardown")
    def test_homepageTitle(self,setup_teardown):
        self.driver=setup_teardown
        self.logger.warning('**Test_001_Login**')
        self.logger.critical('**Home page Title is verifing**')
        self.driver=webdriver.Chrome()
        self.driver.get(self.BaseUrl)
        actual_title = self.driver.title
        if actual_title == 'Your store. Login':
            self.logger.error('**Title is verified**')
            assert True
        else:
            self.logger.debug('**Title is not matched**')
            assert False

        time.sleep(10)
        self.driver.quit()
    
    def test_Login(self,setup_teardown):
        self.driver=setup_teardown
        self.driver=webdriver.Chrome()
        self.driver.get(self.BaseUrl)
        self.lp=LoginPage(self.driver)

        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        time.sleep(5)
        self.driver.quit()
        
    def test_facebook(self,setup_teardown):
        self.driver=setup_teardown
        self.driver.get('https://www.facebook.com')
        time.sleep(3)
        self.driver.quit()
    

