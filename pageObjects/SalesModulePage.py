from selenium.webdriver.common.by import By

from pageObjects.SOCreationPage import SOCreationPage



class SalesModulePage:
    def __init__(self, driver):
        self.driver = driver

    salesOrderOption = (By.XPATH, "//a[text()='Sales Order']")
    addSalesOrder = (By.XPATH, "//a[@href='/admin/sales_orders/new']")

    def getSalesOrderOption(self):
        return self.driver.find_element(*SalesModulePage.salesOrderOption).click()

    def getAddNewSalesOrder(self):
        self.driver.find_element(*SalesModulePage.addSalesOrder).click()
        socreationpage = SOCreationPage(self.driver)
        return socreationpage




