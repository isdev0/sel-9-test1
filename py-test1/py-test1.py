import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope='module')
def driver_ff(request):
    wd = webdriver.Firefox()
    #    request.addfinalizer(wd.quit)
    return wd

@pytest.fixture(scope='module')
def driver_chr(request):
    wd = webdriver.Chrome()
    #    request.addfinalizer(wd.quit)
    return wd

def test_browser_start_ff(driver_ff):
    WebDriverWait(driver_ff,0)

def test_browser_start_chr(driver_chr):
    WebDriverWait(driver_chr,0)