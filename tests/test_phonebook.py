import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v135.debugger import pause
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pages.loginForm import loginForm
from pages.homePage import homePage
from pages.contactPage import contactPage


def test_LoginPositiveTests(driver):#driver--fixture 1
    homepage=homePage(driver)
    homepage.openSite()
    homepage.clickLoginBtn()

    loginform=loginForm(driver)
    loginform.fillLoginForm()
    loginform.clickLogin()

    homepage.checkLoginSuccess(1)


def test_addContactPositiveTest(login):#login -- fixture1
    homepage = homePage(login)
    homepage.clickContactBtn()

    contactpage=contactPage(login)
    contactpage.fillInAllFields()
    contactpage.clickSaveBtn()
    time.sleep(5)

    #NEED TO SCROLL TO THE LAST ELEMENT AND THEN ASSERT IT contactpage.scroll_to_contact('Dasha')

    contactpage.checkAdding('Dasha')

def test_deleteContactPositiveTest(addContact):#login -- fixture1
    homepage = homePage(addContact)



