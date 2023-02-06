import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.settings import DEFAULT_LOCATOR_TYPE


class BasePage():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def field_send_keys(self, selector, value, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, selector).send_keys(value)

    def click_on_the_element(self, selector, selector_type=By.XPATH):
        return self.driver.find_element(selector_type, selector).click()

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def assert_element_text(self, driver, xpath, expected_text):
        """Comparing expected text with observed value from web element
            :param driver: webdriver instance
            :param xpath: xpath to element with text to be observed
            :param expected_text: text what we expecting to be found
            :return: None
        """
        element = driver.find_element(by=By.XPATH, value=xpath)
        element_text = element.text
        assert expected_text == element_text

    def wait_for_visibility_of_element_located(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((locator_type, locator)))

    #def screenshoot_method(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        WebDriver.save_screenshot(self.driver,':\Users\Admin\Documents\GitHub\challenge_portfolio_1\test_cases\screenshots\' + name_screenshot)

