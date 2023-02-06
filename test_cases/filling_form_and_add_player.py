import os
import time
import unittest
from selenium import webdriver

from pages.addAMatch import AddAMatch
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from test_cases.Add_a_player import TestAddNewPlayer
from test_cases.login_to_the_system import TestLoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class FillingAForm(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_filling_A_Form(self):
        TestAddNewPlayer.test_log_in_to_the_system(self)
        filling_text = AddAMatch(self.driver)
        filling_text.main_button_is_visible()
        filling_text.filling_a_form('xer@gmail.com', 'John', 'Doe', '01.01.1999', 'head')
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()