from selenium.webdriver.common.by import By


class AreaPage:

    def __init__(self, driver):
        self.driver = driver

    def open (self, url):
        self.driver.get(url)

    def enter_text(self, id, text):
        self.driver.find_element(By.ID, id).send_keys(text)

    def click_by_id(self, id):
        self.driver.find_element(By.ID, id).click()

    def check_text_is(self, id, text):
        assert self.driver.find_element(By.ID, id).text == text