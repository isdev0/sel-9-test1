import pytest
from selenium import webdriver

@pytest.fixture(scope='module')
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_stickers_count(driver):
    driver.get('http://rubberducks.com:8880/litecart/')
    locator_goods  = '.product.column.shadow.hover-light'
    locator_sticker = 'div.sticker'

    goods = driver.find_elements_by_css_selector(locator_goods)

    for item in goods:
        stickers = item.find_elements_by_css_selector(locator_sticker)
        assert(len(stickers)==1)
