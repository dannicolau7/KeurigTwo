from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver


class KeurigCoupon():
    def __init__(self, driver):
        self.driver = driver

    def couponform(self, couponSingUp):
        coupon_form = self.driver.find_element(By.XPATH, '//input[@id="couponsSignup"]').send_keys(couponSingUp)
        coupon_form = self.driver.find_element(By.XPATH, '//input[@id ="popup_signupbutton"]').click()
        sleep(3)

