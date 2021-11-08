#Implementation of Selenium WebDriver with Python using PyTest
 
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

ch_capabilities = {
        "build" : "Porting test to LambdaTest Selenium Grid (Firefox)",
        "name" : "Porting test to LambdaTest Selenium Grid (Firefox)",
        "platform" : "Windows 10",
        "browserName" : "Chrome",
        "version" : "92.0"
}

def test_lambdatest_google():
    # Profile Link - https://accounts.lambdatest.com/detail/profile
    user_name = "user_name"
    app_key = "access_key"

    remote_url = "http://" + user_name + ":" + app_key + "@hub.lambdatest.com/wd/hub"

    chrome_driver = webdriver.Remote(command_executor = remote_url, desired_capabilities = ch_capabilities)
    
    chrome_driver.get('https://www.google.com')
    chrome_driver.maximize_window()
    
    sleep(5)
    chrome_driver.quit()