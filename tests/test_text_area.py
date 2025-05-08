from pages.text_area_page import AreaPage

def test_input_text(driver):
    area = AreaPage(driver)
    area.open("https://www.qa-practice.com/elements/textarea/single")
    area.enter_text('id_text_area', 'Single area')
    area.click_by_id('submit-id-submit')
    area.check_text_is('result-text', 'Single area')

def test_input_in_multiplate_textareas(driver):
    area = AreaPage(driver)
    area.open('https://www.qa-practice.com/elements/textarea/textareas')
    area.enter_text('id_first_chapter', 'Textarea first chapter')
    area.enter_text('id_second_chapter', 'Textarea second chapter')
    area.enter_text('id_third_chapter', 'Textarea third chapter')
    area.click_by_id('submit-id-submit')
    area.check_text_is('result-text', 'Textarea first chapter\nTextarea second chapter\nTextarea third chapter')