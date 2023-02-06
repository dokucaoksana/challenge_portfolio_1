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



class NegativePass(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)



    def test_negative_pass(self):
        negative_pass = LoginPage(self.driver)
        negative_pass.type_in_email('user01@getnada.com')
        negative_pass.type_in_password('Test-125')
        negative_pass.click_on_the_sign_in_button()
        negative_pass.compare_warning_text()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
