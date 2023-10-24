import time

import pytest

from pageObjects.logoutPage import LogoutPage

from pageObjects.LoginPage import LoginPage
from testData import excelDataSheet
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
        logoutPage = loginpage.getLoginButton()
        log.info("Clicking on Login Button")
        log.info(logoutPage.getProfileImageClick)
        log.info(logoutPage.getLogout)

    @pytest.fixture(params=excelDataSheet.TestData.getTestData("testdata_1"))
    def getData(self, request):
        return request.param
