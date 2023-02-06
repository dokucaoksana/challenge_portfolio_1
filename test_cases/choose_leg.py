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


class ChooseLeg(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_choose_leg(self):
        TestAddNewPlayer.test_log_in_to_the_system(self)
        leg = AddAMatch(self.driver)
        leg.choosing_the_leg()
        time.sleep(3)



    @classmethod
    def tearDown(self):
        self.driver.quit()
