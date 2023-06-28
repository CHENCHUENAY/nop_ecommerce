import pytest
from _pytest import config
from _pytest import *

from selenium import webdriver
import time


@pytest.fixture(autouse = True)
def setup_teardown(browser):
    if browser =='firefox':
        '''thiz fixture will returns the firefox driver'''
        driver = webdriver.Firefox()
        print('Launching firefox Browser')
    elif browser == 'chrome':
        '''thiz fixture will returns the chrome driver'''
        driver =webdriver.Chrome()
        print('Launching chrome Browser')
    elif browser == 'safari':
        '''thiz fixture will returns the safari driver'''
        driver = webdriver.Safari()
        print('Launching safari Browser')
    else:
        driver = webdriver.Chrome()
        print('else part executing ,Launching Browser')
    return driver
    # return driver

def pytest_addoption(parser): #this will get the value from CLI/hooks
    parser.addoption('--browser')
    
@pytest.fixture()
def browser(request): #this will return the browser value to setup method
    return request.config.getoption("--browser")


'''pytest html report'''
# def pytest_configure(config):
    # config._metadata['Protect Name'] = 'nop Commerce'
    # config._metadata['Module Name'] = 'Customers'
    # config._metadata['Tester'] = 'ENAY REDDY'



# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop('JAVA_HOME',None)
#     metadata.pop('Plugins',None)
    

    
    
    
    
    