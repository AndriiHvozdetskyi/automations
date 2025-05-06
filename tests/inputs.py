from conftest import *
from pages.inputpage import InputPage


# Тест введення даних у поле інпуту
def test_input_text(driver):
    inputpage = InputPage(driver)
    inputpage.open("https://www.qa-practice.com/elements/input/simple")
    inputpage.input_text_by_id("id_text_string", "hello")
    inputpage.check_text_by_id("result-text", "hello")

# Тест валідаці на мін к-сть символів
def test_validation_min_character(driver):
    inputpage = InputPage(driver)
    inputpage.open("https://www.qa-practice.com/elements/input/simple")
    inputpage.input_text_by_id("id_text_string", "h")
    inputpage.check_text_by_id("error_1_id_text_string", "Please enter 2 or more characters")

# Тест валідації на макс к-сть символів
def test_validation_max_character(driver):
    inputpage = InputPage(driver)
    inputpage.open("https://www.qa-practice.com/elements/input/simple")
    inputpage.input_text_by_id("id_text_string", "hellohellohellohellohellop")
    inputpage.check_text_by_id("error_1_id_text_string", "Please enter no more than 25 characters")

# Тест відкриття сторінки мейла
def test_open_email_field(driver):
    inputpage = InputPage(driver)
    inputpage.open("https://www.qa-practice.com/elements/input/simple")
    inputpage.click_by_xpath('''//a[text()="Email field"]''')
    inputpage.check_url_is("https://www.qa-practice.com/elements/input/email")

# Тест введення пошти у поле
def test_input_email(driver):
    inputpage = InputPage(driver)
    inputpage.open("https://www.qa-practice.com/elements/input/email")
    inputpage.input_text_by_id("id_email", "dsa@localhost")
    inputpage.check_text_by_id("result-text", "dsa@localhost")

# Тест валідації поля мейлу
def test_validation_email(driver):
    inputpage = InputPage(driver)
    inputpage.open("https://www.qa-practice.com/elements/input/email")
    inputpage.input_text_by_id("id_email", "dsa@dd")
    inputpage.check_text_by_id("error_1_id_email", "Enter a valid email address.")

# Тест відкриття сторінки з паролем
def test_open_password_field(driver):
    inputpage = InputPage(driver)
    inputpage.open("https://www.qa-practice.com/elements/input/email")
    inputpage.click_by_xpath('''//a[text()="Password field"]''')
    inputpage.check_url_is("https://www.qa-practice.com/elements/input/passwd")

# Тест вводу пароля
def test_input_password(driver):
    inputpage = InputPage(driver)
    inputpage.open("https://www.qa-practice.com/elements/input/passwd")
    inputpage.input_text_by_id("id_password", "Aa11111!")
    inputpage.check_text_by_id("result-text", "Aa11111!")

# Тест мін к-сть символів в паролі
def test_validation_min_characters_password(driver):
    inputpage = InputPage(driver)
    inputpage.open("https://www.qa-practice.com/elements/input/passwd")
    inputpage.input_text_by_id("id_password", "Aa111")
    inputpage.check_text_by_id("error_1_id_password", "Low password complexity")

# Тест валідації на відсутність верхнього регістра символів у паролі
def test_validation_uppercase_characters_password(driver):
    inputpage = InputPage(driver)
    inputpage.open("https://www.qa-practice.com/elements/input/passwd")
    inputpage.input_text_by_id("id_password", "aa11111!")
    inputpage.check_text_by_id("error_1_id_password", "Low password complexity")

# Тест валідації на відсутність нижнього регістра символів у паролі
def test_validation_lowercase_characters_password(driver):
    inputpage = InputPage(driver)
    inputpage.open("https://www.qa-practice.com/elements/input/passwd")
    inputpage.input_text_by_id("id_password", "AA11111!")
    inputpage.check_text_by_id("error_1_id_password", "Low password complexity")

# Тест валідації на відсутність цифер у паролі
def test_validation_digit_password(driver):
    inputpage = InputPage(driver)
    inputpage.open("https://www.qa-practice.com/elements/input/passwd")
    inputpage.input_text_by_id("id_password", "Aaaaaaaaa!")
    inputpage.check_text_by_id("error_1_id_password", "Low password complexity")

# Тест валідації на відсутність пец символів у паролі
def test_validation_special_characters_password(driver):
    inputpage = InputPage(driver)
    inputpage.open("https://www.qa-practice.com/elements/input/passwd")
    inputpage.input_text_by_id("id_password", "Aa111111")
    inputpage.check_text_by_id("error_1_id_password", "Low password complexity")