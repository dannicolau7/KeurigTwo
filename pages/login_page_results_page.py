from time import sleep

from selenium.webdriver.common.by import By

class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    def loginkeurig(self, loginKeurig):
        self.driver.find_element(By.XPATH, '//*[@id="_tealiumModalClose"]').click()

        self.driver.find_element(By.XPATH, '(//div[@class ="subMenuContainer text-center  css-f1zt5s"])[1]').click()

        self.driver.find_element(By.XPATH,
                                 '//*[@id="login-tabs-section-tabpane-logIn"]/section/form/div[3]/div[1]/label/span').click()

        self.driver.find_element(By.XPATH,
                                 '//*[@id="login-tabs-section-tabpane-logIn"]/section/form/div[1]/input').send_keys(
            loginKeurig)
    def password(self, PassWord):
        self.driver.find_element(By.XPATH, '//*[@id="L_Password"]').send_keys(PassWord)

        self.driver.find_element(By.XPATH, '//*[@id="login-tabs-section-tabpane-logIn"]/section/form/button').click()
        sleep(3)

    def starterkit(self):
        self.driver.find_element(By.XPATH, '//a[@title=" Keurig® Starter Kit"]/div[@class="oz-hide-in-mobile"]').click()

        self.driver.find_element(By.XPATH, '//div[@data-at-id="dealsComponent"]').click()

        self.driver.find_element(By.XPATH,
                                 '//a[@href="/content/auto-delivery?open=ad&cm_sp=25off-_-deals+page-_-subscribe"]').click()

        self.driver.find_element(By.XPATH, '//div[@class="s7innercontrolbarcontainer"]').click()

        self.driver.find_element(By.XPATH, '//div[@id="s7_videoview_advideo_mutableVolume"]').click()

    def mainpage(self):
        self.driver.find_element(By.XPATH, '//div[@class="yCmsComponent keurig-logo logo-desktop-only"]').click()

    def search(self, Search):
        self.driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys(Search)

        self.driver.find_element(By.XPATH,
                                 '//*[@class="search-container input-container css-1hp7dkc"]/div[@class="input-group"]').click()

        self.driver.find_element(By.XPATH,
                                 '//div[@class="css-vy5380 col"]/a[@href="/search?text=pod|search_suggestion"]').click()

    def ourmailinglist(self, OurmailingList):
        self.driver.find_element(By.XPATH, '//input[@placeholder="Your email"]').send_keys("OurmailingList")

        self.driver.find_element(By.XPATH, '//*[@class="btn-submit css-nnbjkw"]').click()