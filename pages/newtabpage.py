from selenium.webdriver.common.by import By


class NewTabPage:

    def __init__(self, driver):
        self.driver = driver

    def open_link(self):
        self.driver.get("https://www.qa-practice.com/elements/new_tab/link")

    def open_button(self):
        self.driver.get("https://www.qa-practice.com/elements/new_tab/button")

    def click_by_xpath(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click()

    def click_by_id(self, id):
        self.driver.find_element(By.ID, id).click()

    def find_element_by_tag_name(self, tag_name):
        return self.driver.find_element(By.TAG_NAME, tag_name)


    def switch_to_new_tab(self, original_window):
        windows = self.driver.window_handles
        assert len(windows) == 2
        for handle in windows:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                break

    def check_url_is(self, url):
        assert self.driver.current_url == url

    def check_title_is_by_tag(self, tag, title):
        element_text = self.find_element_by_tag_name(tag).text
        assert element_text == title
