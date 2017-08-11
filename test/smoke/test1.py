import pytest
from selenium import webdriver

@pytest.allure.step
def test1():
    driver = webdriver.Chrome("/usr/bin/chromedriver")