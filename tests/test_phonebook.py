import os
import time


import pytest
from pip._internal.resolution.resolvelib.factory import C
from selenium.webdriver.common.by import By

from pages.contactPage import contactPage
from pages.homePage import homePage
from pages.loginForm import loginForm
import pyautogui

from tests.conftest import capture_screenshot


def test_LoginPositiveTests(driver):#driver--fixture 1
    homepage=homePage(driver)
    homepage.openSite()
    homepage.clickLoginBtn()
    loginform=loginForm(driver)
    loginform.fillLoginForm()
    loginform.clickLogin()
    time.sleep(2)
    homepage.checkLoginSuccess(1)

def test_LoginNegativeTestsWithEmptyEmail(driver):#driver--fixture 1
    homepage=homePage(driver)
    homepage.openSite()
    homepage.clickLoginBtn()
    loginform=loginForm(driver)
    loginform.fillLoginFormWithEmptyEmail()
    loginform.clickLogin()
    time.sleep(2)
    homepage.checkLoginSuccess(1)


def test_addContactPositiveTest(login):#login -- fixture1
    homepage = homePage(login)
    homepage.clickContactBtn()
    contactpage=contactPage(login)
    contactpage.fillInAllFields()
    contactpage.clickSaveBtn()
    time.sleep(5)
    contactpage.checkThatNewContactWasAdded('Dasha')

def test_deleteContactPositiveTest(addContact):
    homepage = homePage(addContact)
    contactpage = contactPage(addContact)
    qty_before = contactpage.countContactsBefore()
    contactpage.clickOnAddedContact()
    contactpage.clickRemoveBtn()
    time.sleep(2)
    contactpage.isContactWasDeleted(qty_before)















        #driver.quit()

#def capture_screenshot(test_name):
   # screenshot_path = os.path.join(os.getcwd(), f"{test_name}_failed.png")
   # screenshot = pyautogui.screenshot()
   # screenshot.save(screenshot_path)
   # print(f"Screenshot saved at: {screenshot_path}")







