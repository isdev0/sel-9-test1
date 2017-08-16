import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope='module')
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_adm_login(driver):
    driver.get('http://rubberducks.com:8880/litecart/admin/')
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()
    WebDriverWait(driver, 5)

def test_menu_list(driver):

    locator_top_menu  = 'ul#box-apps-menu.list-vertical li#app->a'
    locator_sub_menu  = 'ul#box-apps-menu.list-vertical li#app- li:not(.selected)[id^=doc-]>a'
    locator_header_h1 = 'td#content>h1'

    root_menu = driver.find_elements_by_css_selector(locator_top_menu)
    count_root_elements = len(root_menu)

    #for element_menu in root_menu:
    #    print( '\'' + element_menu.get_attribute('innerText') + '\'' )

    for i in range(0, count_root_elements):

        root_menu = driver.find_elements_by_css_selector(locator_top_menu)
        root_menu[i].click()

        title_h1 = driver.find_element_by_css_selector(locator_header_h1).get_attribute('textContent')
        assert(title_h1 != '')

        sub_menu = driver.find_elements_by_css_selector(locator_sub_menu)
        count_sub_elements = len(sub_menu)

        for j in range(0, count_sub_elements):
            sub_menu = driver.find_elements_by_css_selector(locator_sub_menu)
            sub_menu[j].click()

            title_h1 = driver.find_element_by_css_selector(locator_header_h1).get_attribute('textContent')
            assert(title_h1 != '')
