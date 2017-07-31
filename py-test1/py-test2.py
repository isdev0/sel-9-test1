import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope='module')
def driver(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd

def test_adm_login(driver):
    driver.get('http://rubberducks.com:8880/litecart/admin/')
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()
    WebDriverWait(driver, 5)
