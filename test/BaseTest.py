import pytest
from selenium.webdriver.support.wait import WebDriverWait

from core.WebDriverFactory import DriverFactory


class BaseTest(DriverFactory):

    driver = None

    @classmethod
    def setUpClass(cls):
        driver = cls.getDriver()
        cls.driver = driver
        BaseTest.wait = WebDriverWait(driver, 10)
        driver.get('http://www.google.com/')

    @classmethod
    def tearDown(self):
        self.driver.quit()
