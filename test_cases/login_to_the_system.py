import os
import time
import unittest
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from selenium.webdriver.common.by import By
import datetime



class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.wait_for_element_to_be_clickable(locator="//span[normalize-space()='Sign in']")
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        time.sleep(5)


    @classmethod
    def tearDown(self):
        self.driver.quit()