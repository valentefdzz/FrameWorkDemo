import unittest
import pytest
from pages.ui_homepage import homepage
from pages.ui_gamepage import gamepage

@pytest.mark.usefixtures("setup")
class test_one(unittest.TestCase):

    def test_task1(self):
        #Start Browser
        #Verify Main Page is Displayed
        hp = homepage(self.driver)
        self.assertEqual(hp.expected_title(self), hp.actual_title(self), "Home page did not load")

        #Click Here Link
        hp.click_here(self)

        #Verify Game Page is Diplayed
        gp = gamepage(self.driver)
        gp.cancel_button_wait(self)
        self.assertEqual(True, gp.cancel_button(self).is_displayed(), "Game page did not load")

        #Click Help Button
        gp.click_help(self)

        #Verify Help Response is Displayed
        self.assertEqual(True, gp.help_response(self).is_displayed(), "Help response not displayed")

    def tearDown(self):
         self.driver.close

if __name__ == '__main__':
     unittest.main()


