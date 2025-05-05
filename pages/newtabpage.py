from selenium.webdriver.common.by import By


class NewTabPage:

    def __init__(self, driver):
        self.driver = driver

    def open_link(self):
        self.driver.get("https://www.qa-practice.com/elements/new_tab/link")

    def open_button(self):
        self.driver.get("https://www.qa-practice.com/elements/new_tab/button")

    def find_element_by_xpath_and_click(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click()

    def find_element_by_id_and_click(self, id):
        self.driver.find_element(By.ID, id).click()

    def find_page_url(self, original_window):
        windows = self.driver.window_handles
        assert len(windows) == 2
        for handle in windows:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                break