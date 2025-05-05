from selenium.webdriver.common.by import By
from conftest import driver
from pages.newtabpage import NewTabPage

# Тест відкриття цієї сторінки
def test_open_site(driver):
    newtabpage = NewTabPage(driver)
    newtabpage.open_link()
    header_text = driver.find_element(By.TAG_NAME, "h1")
    assert header_text.text == "Open link in a new tab"

# Відкриття нового табу кнопкою
def test_click_newtab(driver):
    newtabpage = NewTabPage(driver)
    newtabpage.open_link()
    newtabpage.find_element_by_xpath_and_click('''//a[text()="New tab button"]''')
    assert driver.current_url == "https://www.qa-practice.com/elements/new_tab/button"

# відкриття новго табу з лінкою
def test_click_newtablink(driver):
    newtabpage = NewTabPage(driver)
    newtabpage.open_button()
    newtabpage.find_element_by_xpath_and_click('''//a[text()="New tab link"]''')
    assert driver.current_url == "https://www.qa-practice.com/elements/new_tab/link"

# Відкриття нової сторінки кліком на урлу
def test_click_linknewpage(driver):
    newtabpage = NewTabPage(driver)
    newtabpage.open_link()
    original_window = driver.current_window_handle
    newtabpage.find_element_by_xpath_and_click('''//a[text()="New page will be opened on a new tab"]''')
    newtabpage.find_page_url(original_window)
    assert driver.current_url == "https://www.qa-practice.com/elements/new_tab/new_page"

# Відкриття нової сторінки кліком на кнопку
def test_click_buttonnewpage(driver):
    newtabpage = NewTabPage(driver)
    newtabpage.open_button()
    original_window = driver.current_window_handle
    newtabpage.find_element_by_id_and_click("new-page-button")
    newtabpage.find_page_url(original_window)
    assert driver.current_url == "https://www.qa-practice.com/elements/new_tab/new_page"