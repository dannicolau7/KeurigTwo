import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("before_start")
class TestHomePage():
    def test_home_page(self):
        self.driver.find_element(By.XPATH, '//input[@id="couponsSignup"]').send_keys("dan.nicolau_ex@kdrp.com")

        self.driver.find_element(By.XPATH, '//input[@id ="popup_signupbutton"]').click()

        self.driver.find_element(By.XPATH, '//*[@id="_tealiumModalClose"]').click()

        self.driver.find_element(By.XPATH, '(//div[@class ="subMenuContainer text-center  css-f1zt5s"])[1]').click()

        self.driver.find_element(By.XPATH,
                            '//*[@id="login-tabs-section-tabpane-logIn"]/section/form/div[3]/div[1]/label/span').click()

        self.driver.find_element(By.XPATH,
                            '//*[@id="login-tabs-section-tabpane-logIn"]/section/form/div[1]/input').send_keys(
            "dan.nicolau_ex@kdrp.com")

        links = self.driver.find_elements(By.TAG_NAME, 'a')
        print(len(links))

        self.driver.find_element(By.XPATH, '//*[@id="L_Password"]').send_keys("D@nn2604")

        self.driver.find_element(By.XPATH, '//*[@id="login-tabs-section-tabpane-logIn"]/section/form/button').click()

        self.driver.find_element(By.XPATH, '//a[@title=" Keurig® Starter Kit"]/div[@class="oz-hide-in-mobile"]').click()

        self.driver.find_element(By.XPATH, '//div[@data-at-id="dealsComponent"]').click()

        self.driver.find_element(By.XPATH,
                            '//a[@href="/content/auto-delivery?open=ad&cm_sp=25off-_-deals+page-_-subscribe"]').click()

        self.driver.find_element(By.XPATH, '//div[@class="s7innercontrolbarcontainer"]').click()

        self.driver.find_element(By.XPATH, '//div[@id="s7_videoview_advideo_mutableVolume"]').click()

        self.driver.find_element(By.XPATH, '//div[@class="yCmsComponent keurig-logo logo-desktop-only"]').click()

        self.driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys("pods")

        self.driver.find_element(By.XPATH,
                            '//*[@class="search-container input-container css-1hp7dkc"]/div[@class="input-group"]').click()

        self.driver.find_element(By.XPATH,
                            '//div[@class="css-vy5380 col"]/a[@href="/search?text=pod|search_suggestion"]').click()

        self.driver.find_element(By.XPATH, '//input[@placeholder="Your email"]').send_keys("dan.nicolau_ex@kdrp.com")

        self.driver.find_element(By.XPATH, '//*[@class="btn-submit css-nnbjkw"]').click()
