import pytest
from selenium.webdriver.common.by import By
from pages.keurig_coupon_page import KeurigCoupon
from selenium.webdriver.support.wait import WebDriverWait
import time

from pages.login_page_results_page import LoginPage


@pytest.mark.usefixtures("before_start")
class TestHomePage:
    def test_home_page(self):
        # couponsingup
        kc = KeurigCoupon(self.driver)
        kc.couponform("dan.nicolau_ex@kdrp.com")
        #loginKeurig
        lk = LoginPage(self.driver)
        lk.loginkeurig("dan.nicolau_ex@kdrp.com")
        ps = LoginPage(self.driver)
        ps.password("Poiu@1234")
        #sellect Starter Kit
        st = LoginPage(self.driver)
        st.starterkit()
        # back to main page
        mp = LoginPage(self.driver)
        mp.mainpage()
        #Search
        sh = LoginPage(self.driver)
        sh.search("pods")
        #Join our mailing list
        ml = LoginPage(self.driver)
        ml.ourmailinglist("dan.nicolau_ex@kdrp.com")

        links = self.driver.find_elements(By.TAG_NAME, 'a')
        print(len(links))