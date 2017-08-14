from enum import Enum
import unittest

from selenium.webdriver import DesiredCapabilities
from selenium import webdriver


class DriverType(Enum):
    def CHROME(self):
        capabilities = DesiredCapabilities().CHROME
        return webdriver.Chrome()

    def FIREFOX(self):
        capabilities = DesiredCapabilities().FIREFOX
        return webdriver.Firefox()


class DriverFactory(unittest.TestCase):
    webdriver = None

    @staticmethod
    def instantiateDriverObject():
        webdriver = DriverThread().getDriver()

    @staticmethod
    def getDriver():
        #webdriver.instantiateDriverObject()
        return DriverThread().getDriver()


class DriverThread():
    webDriver = None
    driverType = None
    browser = "CHROME"
    defaultDriverType = DriverType.CHROME

    def getDriver(self):
        driver_type = self.determineEffectiveDriverType()
        driver = self.instantiateWebDriver(driver_type)
        return driver

    def instantiateWebDriver(self, driver_type):
        self.webDriver = driver_type
        return self.webDriver

    def determineEffectiveDriverType(self):
        self.driverType = self.defaultDriverType
        # //TODO complete >
        return webdriver.Chrome()
