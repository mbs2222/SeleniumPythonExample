from selenium import webdriver
import pytest

#Test setup and teardown using pytest
@pytest.fixture()
def test_setup():
    # Test setup (executed before any test)
    global driver #"driver" must be global: It is used in all functions
    driver = webdriver.Chrome(executable_path="C:/Users/medbe/Documents/Automation Testing/SeleniumProject/SeleniumWebdrivers/chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    #Test teardown (exectued after any test)
    yield
    driver.quit()
    print("Test Completed")

def test_login(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()


