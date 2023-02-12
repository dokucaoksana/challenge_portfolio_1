import unittest
from unittest.loader import makeSuite
from test_cases.Add_a_player import AddPlayer
from test_cases.filling_form_and_add_player import FillingAForm
from test_cases.change_language import ChangeLanguage
from test_cases.choose_leg import ChooseLeg
from test_cases.login_to_the_system import TestLoginPage
from test_cases.negative_pass import NegativePass
from test_cases.sign_out import SigningOut

from test_cases.framework import Test



def full_suite():

   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(AddPlayer))
   test_suite.addTest(makeSuite(ChangeLanguage))
   test_suite.addTest(makeSuite(ChooseLeg))
   test_suite.addTest(makeSuite(FillingAForm))
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(NegativePass))
   test_suite.addTest(makeSuite(SigningOut))
   return test_suite





if __name__ == '__main__':

   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())