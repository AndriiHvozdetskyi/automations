from selenium.webdriver.common.by import By
from conftest import driver

# Тест відкриття цієї сторінки
def test_open_site(driver):
    driver.get("https://www.qa-practice.com/elements/new_tab/link")
    header_text = driver.find_element(By.TAG_NAME, "h1")
    assert header_text.text == "Open link in a new tab"

# Відкриття нового табу кнопкою
def test_click_newtab(driver):
    driver.get("https://www.qa-practice.com/elements/new_tab/link")
    button_tab = driver.find_element(By.XPATH, value='''//a[text()="New tab button"]''')
    button_tab.click()
    assert driver.current_url == "https://www.qa-practice.com/elements/new_tab/button"

# відкриття новго табу з лінкою
def test_click_newtablink(driver):
    driver.get("https://www.qa-practice.com/elements/new_tab/button")
    button_tab = driver.find_element(By.XPATH, value='''//a[text()="New tab link"]''')
    button_tab.click()
    assert driver.current_url == "https://www.qa-practice.com/elements/new_tab/link"

# Відкриття нової сторінки кліком на урлу
def test_click_linknewpage(driver):
    driver.get("https://www.qa-practice.com/elements/new_tab/link")
    original_window = driver.current_window_handle
    link_click = driver.find_element(By.XPATH, value='''//a[text()="New page will be opened on a new tab"]''')
    link_click.click()
    windows = driver.window_handles
    assert len(windows) == 2
    for handle in windows:
        if handle != original_window:
            driver.switch_to.window(handle)
            break
    assert driver.current_url == "https://www.qa-practice.com/elements/new_tab/new_page"

# Відкриття нової сторінки кліком на кнопку
def test_click_buttonnewpage(driver):
    driver.get("https://www.qa-practice.com/elements/new_tab/button")
    original_window = driver.current_window_handle
    button_click = driver.find_element(By.ID, value='new-page-button')
    button_click.click()
    windows = driver.window_handles
    assert len(windows) == 2
    for handle in windows:
        if handle != original_window:
            driver.switch_to.window(handle)
            break
    assert driver.current_url == "https://www.qa-practice.com/elements/new_tab/new_page"