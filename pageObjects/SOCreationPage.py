from selenium.webdriver.common.by import By


class SOCreationPage:
    def __init__(self, driver):
        self.driver = driver

    buyerPartContainer = (By.ID, 'select2-sales_order_buyer_party_id-container')

    enterBuyerParty = (By.CSS_SELECTOR, 'input.select2-search__field[aria-controls="select2-sales_order_buyer_party_id-results"]')

    selectBuyerParty = (By.CSS_SELECTOR, '.select2-results__option')

    buyerPoNumber = (By.ID, 'sales_order_po_number')

    internalSkuContainer = (By.XPATH, '//span[@aria-labelledby="select2-sales_order_sales_order_items_attributes_0_master_sku_id-container"]')

    enterInternalSku = (By.CSS_SELECTOR, 'input.select2-search__field[aria-controls="select2-sales_order_sales_order_items_attributes_0_master_sku_id-results"]')

    selectInternalSku = (By.XPATH, '//li[@class="select2-results__option"][1]')

    saveDraft = (By.ID, 'so_submit')

    confirmSoButton =(By.XPATH, '//a[text()="Confirm SO"]')

    def getClickOnBuyerPartyContainer(self):
        return self.driver.find_element(*SOCreationPage.buyerPartContainer).click()

    def getEnterBuyerParty(self):
        return self.driver.find_element(*SOCreationPage.enterBuyerParty)

    def getSelectBuyerParty(self):
        return self.driver.find_element(*SOCreationPage.selectBuyerParty).click()

    def getBuyerPoNumber(self):
        return self.driver.find_element(*SOCreationPage.buyerPoNumber)

    def getClickOnInternalSku(self):
        return self.driver.find_element(*SOCreationPage.internalSkuContainer).click()

    def getEnterInternalSku(self):
        return self.driver.find_element(*SOCreationPage.enterInternalSku)

    def getSelectInternalSku(self):
        return self.driver.find_element(*SOCreationPage.selectInternalSku).click()

    def getSaveDraftButton(self):
        return self.driver.find_element(*SOCreationPage.saveDraft).click()

    def getConfirmSoButton(self):
        return  self.driver.find_element(*SOCreationPage.confirmSoButton).click()
