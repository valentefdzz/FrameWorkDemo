import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
import pytest

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    wait = WebDriverWait(driver, 10)
    driver.get("https://userinyerface.com/")
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    driver.close()