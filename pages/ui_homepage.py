from selenium.webdriver.common.by import By

class homepage():
    def __init__(self, driver):
        self.driver = driver
        self.title_xp = '//html//head//title'
        self.here_xp = '//div//div[1]//div//div[4]//p//a'
        self.exp_title_xp = "User Inyerface - A worst-practice UI experiment"

    def actual_title(self, element):
        element = self.driver.find_element(By.XPATH, str(self.title_xp))

    def expected_title(self, element):
        element = str(self.exp_title_xp)

    def click_here(self, element):
        element = self.driver.find_element(By.XPATH, str(self.here_xp)).click()
