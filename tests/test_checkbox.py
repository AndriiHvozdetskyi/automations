from pages.checkbox_pages import CheckBox

#Тест активації 1 чекбоксу та перегляд результату
def test_click_with_active_checkbox(driver):
    checkbox = CheckBox(driver)
    checkbox.open("https://www.qa-practice.com/elements/checkbox/single_checkbox")
    checkbox.click_by_id("id_checkbox_0")
    checkbox.click_by_id("submit-id-submit")
    checkbox.check_text_is("result-text", "select me or not")

#Тест відкриття сторінки з чекбоксами через таб
def test_open_page_checkboxes(driver):
    checkbox = CheckBox(driver)
    checkbox.open("https://www.qa-practice.com/elements/checkbox/single_checkbox")
    checkbox.click_by_xpath('//a[text()="Checkboxes"]')
    checkbox.check_url_is("https://www.qa-practice.com/elements/checkbox/mult_checkbox")

#Тест вибір 1-го чекбоксу
def test_click_first_checkbox(driver):
    checkbox = CheckBox(driver)
    checkbox.open("https://www.qa-practice.com/elements/checkbox/mult_checkbox")
    checkbox.click_by_id("id_checkboxes_0")
    checkbox.click_by_id("submit-id-submit")
    checkbox.check_text_is("result-text", "one")

#Тест вибір 2-го чекбоксу
def test_click_second_checkbox(driver):
    checkbox = CheckBox(driver)
    checkbox.open("https://www.qa-practice.com/elements/checkbox/mult_checkbox")
    checkbox.click_by_id("id_checkboxes_1")
    checkbox.click_by_id("submit-id-submit")
    checkbox.check_text_is("result-text", "two")

#Тест вибір 3-го чекбоксу
def test_click_third_checkbox(driver):
    checkbox = CheckBox(driver)
    checkbox.open("https://www.qa-practice.com/elements/checkbox/mult_checkbox")
    checkbox.click_by_id("id_checkboxes_2")
    checkbox.click_by_id("submit-id-submit")
    checkbox.check_text_is("result-text", "three")

#Тест вибір усіх чекбоксів та перевірка результату
def test_multiselect_checkboxes(driver):
    checkbox = CheckBox(driver)
    checkbox.open("https://www.qa-practice.com/elements/checkbox/mult_checkbox")
    checkbox.click_by_id("id_checkboxes_0")
    checkbox.click_by_id("id_checkboxes_1")
    checkbox.click_by_id("id_checkboxes_2")
    checkbox.click_by_id("submit-id-submit")
    checkbox.check_text_is("result-text", "one, two, three")