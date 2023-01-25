import unittest
import pytest
from pages.ui_homepage import homepage
from pages.ui_gamepage import gamepage

@pytest.mark.usefixtures("setup")
class test_three(unittest.TestCase):

    def test_task3(self):
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

        #input data to form
        gp.fill_invalid_password(self)
        gp.fill_email(self)
        gp.fill_domain(self)
        gp.click_other_button(self)
        # accept terms and conditions
        gp.accept_terms(self)
        # click next
        gp.click_next(self)
        #verify second card is open
        self.assertEqual(True, gp.avatar_image(self).is_displayed(),"Second card did not open")

    def tearDown(self):
         self.driver.close

if __name__ == '__main__':
     unittest.main()

