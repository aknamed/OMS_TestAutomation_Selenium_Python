from selenium.webdriver.common.by import By


class LogoutPage:

    def __init__(self, driver):
        self.driver = driver

    profileImage = (By.CSS_SELECTOR, ".img-profile")
    logout = (By.LINK_TEXT, "Logout")

    def getProfileImageClick(self):
        return self.driver.find_element(*LogoutPage.profileImage).click()

    def getLogout(self):
        return self.driver.find_element(*LogoutPage.logout).click()
