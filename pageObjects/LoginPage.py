from selenium.webdriver.common.by import By

from pageObjects.LandingPage import LandingPage


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "user_email")
    password = (By.ID, "user_password")
    loginBtn = (By.NAME, "commit")

    def getUserName(self):
        return self.driver.find_element(*LoginPage.username)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def getLoginButton(self):
        self.driver.find_element(*LoginPage.loginBtn).click()
        self.driver.implicitly_wait(2)
        landingpage = LandingPage(self.driver)
        return landingpage

