from selenium.webdriver.common.by import By

from pageObjects.SalesModulePage import SalesModulePage


class LandingPage:
    def __init__(self, driver):
        self.driver = driver

    salesTab = (By.ID, "navbarDropdownSales")

    def getSalesTab(self):
        self.driver.find_element(*LandingPage.salesTab).click()
        salesmodulepage = SalesModulePage(self.driver)
        return salesmodulepage

