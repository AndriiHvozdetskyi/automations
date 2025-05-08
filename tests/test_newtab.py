from conftest import driver
from pages.newtabpage import NewTabPage

# Тест відкриття цієї сторінки
def test_open_site(driver):
    newtabpage = NewTabPage(driver)
    newtabpage.open_link()
    newtabpage.check_title_is_by_tag("h1", "Open link in a new tab")

# Відкриття нового табу кнопкою
def test_click_newtab(driver):
    newtabpage = NewTabPage(driver)
    newtabpage.open_link()
    newtabpage.click_by_xpath('''//a[text()="New tab button"]''')
    newtabpage.check_url_is("https://www.qa-practice.com/elements/new_tab/button")

# відкриття новго табу з лінкою
def test_click_newtablink(driver):
    newtabpage = NewTabPage(driver)
    newtabpage.open_button()
    newtabpage.click_by_xpath('''//a[text()="New tab link"]''')
    newtabpage.check_url_is("https://www.qa-practice.com/elements/new_tab/link")

# Відкриття нової сторінки кліком на урлу
def test_click_linknewpage(driver):
    newtabpage = NewTabPage(driver)
    newtabpage.open_link()
    original_window = driver.current_window_handle
    newtabpage.click_by_xpath('''//a[text()="New page will be opened on a new tab"]''')
    newtabpage.switch_to_new_tab(original_window)
    newtabpage.check_url_is("https://www.qa-practice.com/elements/new_tab/new_page")

# Відкриття нової сторінки кліком на кнопку
def test_click_buttonnewpage(driver):
    newtabpage = NewTabPage(driver)
    newtabpage.open_button()
    original_window = driver.current_window_handle
    newtabpage.click_by_id("new-page-button")
    newtabpage.switch_to_new_tab(original_window)
    newtabpage.check_url_is("https://www.qa-practice.com/elements/new_tab/new_page")