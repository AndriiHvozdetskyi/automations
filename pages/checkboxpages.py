from selenium.webdriver.common.by import By

class CheckBox:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def click_by_id(self, id):
        self.driver.find_element(By.ID, id).click()

    def click_by_xpath(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click()

    def check_text_is(self, id, text):
        assert self.driver.find_element(By.ID, id).text == text

    def check_url_is(self, url):
        assert self.driver.current_url == url