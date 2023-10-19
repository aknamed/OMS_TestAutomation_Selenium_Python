import time

import pytest

from pageObjects.LoginPage import LoginPage
from testData.loginData import loginData
from utilities.BaseClass import BaseClass


class TestLogin(BaseClass):

    def test_login(self, getData):
        loginpage = LoginPage(self.driver)
        log = self.getLogger()
        loginpage.getUserName().send_keys(getData["username"])
        log.info("Entering EmailId of User")
        loginpage.getPassword().send_keys(getData["password"])
        log.info("Entering Password")
        landingpage = loginpage.getLoginButton()
        log.info("Clicking on Login Button")
        salesmodulepage = landingpage.getSalesTab()
        salesmodulepage.getSalesOrderOption()
        socreationpage = salesmodulepage.getAddNewSalesOrder()
        socreationpage.getClickOnBuyerPartyContainer()
        socreationpage.getEnterBuyerParty().send_keys("chai testing hospital")
        time.sleep(3)
        socreationpage.getSelectBuyerParty()
        socreationpage.getBuyerPoNumber().send_keys("Test_123")
        time.sleep(2)
        socreationpage.getClickOnInternalSku()
        time.sleep(2)
        socreationpage.getEnterInternalSku().send_keys("CHAI AUTO TEST 1")
        time.sleep(2)
        socreationpage.getSelectInternalSku()
        time.sleep(2)
        socreationpage.getSaveDraftButton()
        time.sleep(2)
        socreationpage.getConfirmSoButton()

    @pytest.fixture(params=loginData.testLoginData)
    def getData(self, request):
        return request.param
