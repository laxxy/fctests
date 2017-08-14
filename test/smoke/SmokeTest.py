import pytest
from selenium import webdriver

from test.BaseTest import BaseTest


class SmokeTest(BaseTest):

    @pytest.allure.step
    def test1(self):
        selector = self.driver.find_element_by_css_selector(".content")
