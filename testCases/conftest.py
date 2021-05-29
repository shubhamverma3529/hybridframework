from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome(executable_path="C:/Users/shubh/Downloads/chromedriver_win32/chromedriver.exe")
    elif browser=='firefox':
        driver = webdriver.Firefox(executable_path="C:/Users/shubh/Downloads/geckodriver-v0.29.1-win64/geckodriver.exe")
    else:
        driver=webdriver.Chrome(executable_path="C:/Users/shubh/Downloads/chromedriver_win32/chromedriver.exe")
    return driver

def pytest_addoption(parser):    # this will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # This will return the browser value to setup method
    return request.config.getoption("--browser")

################### Pytest HTML Report ############################################

#It is hook for adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Shubham'

#It is hook to delete/modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
