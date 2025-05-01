from selenium.webdriver.common.by import By
from conftest import driver


def test_open_site(driver):
    driver.get("https://www.qa-practice.com/elements/new_tab/link")
    header_text = driver.find_element(By.TAG_NAME, "h1")
    assert header_text.text == "Open link in a new tab"