from selenium.webdriver.common.by import By

from conftest import driver


class AlertsPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def click_by_xpath(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click()

    def submit_alerts(self):
        self.driver.switch_to.alert.accept()

    def dismiss_alerts(self):
        self.driver.switch_to.alert.dismiss()

    def input_text_in_alerts(self, text):
        self.driver.switch_to.alert.send_keys(text)

    def check_text_is(self, id, text):
        assert self.driver.find_element(By.ID, id).text == text