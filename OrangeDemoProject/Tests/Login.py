from selenium import webdriver
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from OrangeDemoProject.Pages.LoginPage import LoginPage

class test_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/medbe/Documents/Automation Testing/SeleniumProject/SeleniumWebdrivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed")

    def test_login(self):
        driver = self.driver
        login = LoginPage(driver)
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

if __name__=='__main__':
    unittest.main

