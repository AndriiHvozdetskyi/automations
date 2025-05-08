from pages.buttons_page import ButtunsPage

#Тест натиску на кнопку
def test_click_button_simple(driver):
    buttonspage = ButtunsPage(driver)
    buttonspage.open("https://www.qa-practice.com/elements/button/simple")
    buttonspage.click_by_id("submit-id-submit")
    buttonspage.check_text("result-text", "Submitted")

#Тест відкриття сторінки з елементом по типу кнопки
def test_open_page_like_button(driver):
    buttonspage = ButtunsPage(driver)
    buttonspage.open("https://www.qa-practice.com/elements/button/simple")
    buttonspage.click_by_xpath('''//a[text()="Looks like a button"]''')
    buttonspage.check_url_is("https://www.qa-practice.com/elements/button/like_a_button")

#Тест натиск на елемент по типу кнопки
def test_click_like_a_button(driver):
    buttonspage = ButtunsPage(driver)
    buttonspage.open("https://www.qa-practice.com/elements/button/like_a_button")
    buttonspage.click_by_xpath('''//a[text()="Click"]''')
    buttonspage.check_text("result-text", "Submitted")

#Тест відкриття сторінки з заблокованою кнопкоб
def test_open_page_disable(driver):
    buttonspage = ButtunsPage(driver)
    buttonspage.open("https://www.qa-practice.com/elements/button/like_a_button")
    buttonspage.click_by_xpath('''//a[text()="Disabled"]''')
    buttonspage.check_url_is("https://www.qa-practice.com/elements/button/disabled")

#Тест активація кнопки через селектор та її натиск
def test_click_disable(driver):
    buttonspage = ButtunsPage(driver)
    buttonspage.open("https://www.qa-practice.com/elements/button/disabled")
    buttonspage.select("id_select_state", "enabled")
    buttonspage.click_by_id("submit-id-submit")
    buttonspage.check_text("result-text", "Submitted")