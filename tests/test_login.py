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
        salesordercreationpage = salesmodulepage.getAddNewSalesOrder()

    @pytest.fixture(params=loginData.testLoginData)
    def getData(self, request):
        return request.param
