import unittest
import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import pytest
from pages.ui_homepage import homepage
from pages.ui_gamepage import gamepage

@pytest.mark.usefixtures("setup")
class test_two(unittest.TestCase):

    def test_task2(self):
        # Start Browser
        # Verify Main Page is Displayed
        hp = homepage(self.driver)
        self.assertEqual(hp.expected_title(self), hp.actual_title(self), "Home page did not load")

        # Click Here Link
        hp.click_here(self)

        #Verify Timer Starting Time
        gp = gamepage(self.driver)
        gp.timer_wait(self)
        self.assertEqual("00:00:00", gp.timer_value(self), "timer Starts from zero")

    def tearDown(self):
        self.driver.close

if __name__ == '__main__':
     unittest.main()
