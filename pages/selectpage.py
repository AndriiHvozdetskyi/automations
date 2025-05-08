from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class SelectPage(object):

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def choose_value(self, id, visible_text):
        Select(self.driver.find_element(By.ID, id)).select_by_visible_text(visible_text)

    def click_by_id(self, id):
        self.driver.find_element(By.ID, id).click()

    def check_text_is(self, id, text):
        assert self.driver.find_element(By.ID, id).text == text