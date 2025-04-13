import os
import time

from pip._internal.resolution.resolvelib.factory import C
from selenium.webdriver.common.by import By

from pages.contactPage import contactPage
from pages.homePage import homePage
from pages.loginForm import loginForm
import pyautogui


def test_LoginPositiveTests(driver):#driver--fixture 1
    homepage=homePage(driver)
    homepage.openSite()
    homepage.clickLoginBtn()
    loginform=loginForm(driver)
    loginform.fillLoginForm()
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






#--------
#contacts_before = driver.find_elements(By.CSS_SELECTOR,'div[class="contact-item_card__2SOIM"]')
   # qty_before = len(contacts_before)
   # print(f"Contacts before deletion: {qty_before}")

   # clickOnContact=driver.find_element(By.CSS_SELECTOR, '[class="contact-page_leftdiv__yhyke"] div:last-child>h2').click()
   # time.sleep(2)
  #  remove = driver.find_element(By.XPATH, '//button[.="Remove"]')
   # remove.click()

   # time.sleep(2)
    #contacts_after = driver.find_elements(By.CSS_SELECTOR,'div[class="contact-item_card__2SOIM"]')
  #  qty_after = len(contacts_after)
  #  print(f"Contacts after deletion: {qty_after}")

    # Assert the difference
  #  assert qty_before-1 == qty_after, "Contact deletion failed!"
#=========












