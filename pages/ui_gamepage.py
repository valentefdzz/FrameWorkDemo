import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from utilities.randomstr import *

class gamepage():
    def __init__(self, driver):
        self.driver = driver
        self.cancel_button_xp = '//div//div[1]//div[2]//div[4]//div//div[1]//div//div[3]//form//div[3]//div[2]//button'
        self.help_button_n = "help-form__help-button"
        self.help_result_xp = '//div//div[1]//div[4]//div//div[2]'
        self.timer_n = "timer"
        self.password_field_xp = '//html//body//div//div[1]//div[2]//div[4]//div//div[1]//div//div[3]//form//div[1]//div[2]//input'
        self.email_field_xp = '//html//body//div//div[1]//div[2]//div[4]//div//div[1]//div//div[3]//form//div[1]//div[3]//div[1]//input'
        self.domain_field_xp = '//html//body//div//div[1]//div[2]//div[4]//div//div[1]//div//div[3]//form//div[1]//div[3]//div[3]//input'
        self.email_other_field_xp = '//html//body//div//div[1]//div[2]//div[4]//div//div[1]//div//div[3]//form//div[1]//div[3]//div[4]//div//div[1]//div[1]'
        self.next_button_n = "Next"
        self.terms_button_xp = '//html//body//div//div[1]//div[2]//div[4]//div//div[1]//div//div[3]//form//div[2]//span//label//span//span'
        self.avatar_box_xp = '//html//body//div//div[1]//div[2]//div[4]//div//div[1]//div//div[2]//div//div[1]//div'
        self.com_button = '//html//body//div//div[1]//div[2]//div[4]//div//div[1]//div//div[3]//form//div[1]//div[3]//div[4]//div//div[2]//div[9]'

    def cancel_button_wait(self, element):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, str(self.cancel_button_xp))))

    def cancel_button(self, element):
        element = self.driver.find_element(By.XPATH, str(self.cancel_button_xp))
        return element

    def click_help(self, element):
        self.driver.find_element(By.CLASS_NAME, self.help_button_n).click()

    def help_response(self, element):
        element = self.driver.find_element(By.XPATH, str(self.help_result_xp))
        return element

    def timer_wait(self, element):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, str(self.timer_n))))

    def timer_value(self, element):
        element = self.driver.find_element(By.CLASS_NAME, str(self.timer_n)).text
        return element

    def fill_password(self, element):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, str(self.password_field_xp))))
        element = self.driver.find_element(By.XPATH, str(self.password_field_xp))
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.DELETE)
        element.send_keys(constant_password)

    def fill_email(self, element):
        element = self.driver.find_element(By.XPATH, str(self.email_field_xp))
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(constant_email)

    def fill_domain(self, element):
        element = self.driver.find_element(By.XPATH, str(self.domain_field_xp))
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(valid_domain)

    def click_other_button(self, element):
        element = self.driver.find_element(By.XPATH, str(self.email_other_field_xp)).click()
        self.driver.find_element(By.XPATH, str(self.com_button)).click()

    def accept_terms(self, element):
        element = self.driver.find_element(By.XPATH, str(self.terms_button_xp)).click()

    def click_next(self, element):
        element = self.driver.find_element(By.LINK_TEXT, self.next_button_n).click()

    def avatar_image(self, element):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, str(self.avatar_box_xp))))
        element = self.driver.find_element(By.XPATH, str(self.avatar_box_xp))
        return element

    def fill_invalid_password(self, element):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, str(self.password_field_xp))))
        element = self.driver.find_element(By.XPATH, str(self.password_field_xp))
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.DELETE)
        element.send_keys(constant_invalid_password)








