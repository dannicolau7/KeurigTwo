import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.core import driver


@pytest.fixture(scope="class")
def before_start(request):
    s = Service('/Users/tetianakravchuk/PycharmProjects/KeuringFramework/chromedriver')
    driver = webdriver.Chrome(service=s)
    #wait = WebDriverWait(driver, 10)
    driver.get("https://www.keurig.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    #request.cls.driver = wait
    yield
    driver.close()


