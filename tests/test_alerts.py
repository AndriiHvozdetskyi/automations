from pages.alerts_page import AlertsPage

def test_confirm_alerts(driver):
    alertspage = AlertsPage(driver)
    alertspage.open("https://www.qa-practice.com/elements/alert/alert#")
    alertspage.click_by_xpath('''//a[text()="Click"]''')
    alertspage.submit_alerts()

def test_confirm_confirmbox(driver):
    alertspage = AlertsPage(driver)
    alertspage.open('https://www.qa-practice.com/elements/alert/confirm#')
    alertspage.click_by_xpath('''//a[text()="Click"]''')
    alertspage.submit_alerts()
    alertspage.check_text_is('result-text', 'Ok')

def test_dismiss_confirmbox(driver):
    alertspage = AlertsPage(driver)
    alertspage.open('https://www.qa-practice.com/elements/alert/confirm#')
    alertspage.click_by_xpath('''//a[text()="Click"]''')
    alertspage.dismiss_alerts()
    alertspage.check_text_is('result-text', 'Cancel')

def test_confirm_input_text_in_allerts(driver):
    alertspage = AlertsPage(driver)
    alertspage.open('https://www.qa-practice.com/elements/alert/prompt')
    alertspage.click_by_xpath('''//a[text()="Click"]''')
    alertspage.input_text_in_alerts('QA Automation')
    alertspage.submit_alerts()
    alertspage.check_text_is('result-text', 'QA Automation')

def test_dismiss_input_text_in_allerts(driver):
    alertspage = AlertsPage(driver)
    alertspage.open('https://www.qa-practice.com/elements/alert/prompt')
    alertspage.click_by_xpath('''//a[text()="Click"]''')
    alertspage.dismiss_alerts()
    alertspage.check_text_is('result-text', 'You canceled the prompt')