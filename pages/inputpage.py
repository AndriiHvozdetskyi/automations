from selenium.webdriver.common.by import By

class InputPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def input_text_by_id(self, id, text):
        self.driver.find_element(By.ID, id).send_keys(text)
        self.driver.find_element(By.ID, id).submit()

    def check_text_by_id(self, id, text):
        assert self.driver.find_element(By.ID, id).text == text

    def click_by_xpath(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click()

    def check_url_is(self, url):
        assert self.driver.current_url == url