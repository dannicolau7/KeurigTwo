import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def before_start(request):
    s = Service('/Users/tetianakravchuk/PycharmProjects/KeuringFramework/chromedriver')
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.keurig.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()
