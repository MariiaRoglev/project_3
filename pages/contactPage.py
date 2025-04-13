from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class contactPage:

    def __init__(self, driver):  # self==page.We saved browser for our page. need to add to all classed (pages)
        self.driver = driver

    def fillInAllFields(self):
        nameField=self.driver.find_element(By.CSS_SELECTOR, 'input:nth-child(1)')
        nameField.click()
        nameField.send_keys('Dasha')

        lastNameField = self.driver.find_element(By.CSS_SELECTOR, 'input:nth-child(2)')
        lastNameField.click()
        lastNameField.send_keys('Dow')

        phoneField = self.driver.find_element(By.CSS_SELECTOR, 'input:nth-child(3)')
        phoneField.click()
        phoneField.send_keys('12345678920')

        emailField = self.driver.find_element(By.CSS_SELECTOR, 'input:nth-child(4)')
        emailField.click()
        emailField.send_keys('qwerty@gmail.com')

        addressField = self.driver.find_element(By.CSS_SELECTOR, 'input:nth-child(5)')
        addressField.click()
        addressField.send_keys('Haifa')

        descriptionField = self.driver.find_element(By.CSS_SELECTOR, 'input:nth-child(6)')
        descriptionField.click()
        descriptionField.send_keys('QA')

    def clickSaveBtn(self):
        clickSaveBtn = self.driver.find_element(By.CSS_SELECTOR, '.add_form__2rsm2 button')
        clickSaveBtn.click()

    def checkThatNewContactWasAdded(self, contact):
        newUserNAme = self.driver.find_element(By.CSS_SELECTOR, '[class="contact-page_leftdiv__yhyke"] div:last-child>h2')
        assert newUserNAme.text == contact
        print(newUserNAme.text+'='+contact)


    def clickOnAddedContact(self):
        clickOnContact = self.driver.find_element(By.CSS_SELECTOR, '[class="contact-page_leftdiv__yhyke"] div:last-child>h2')
        clickOnContact.click()

    def clickRemoveBtn(self):
        removeBtn = self.driver.find_element(By.XPATH, '//button[.="Remove"]')
        removeBtn.click()

    def countContactsBefore(self):
        contacts_before = self.driver.find_elements(By.CSS_SELECTOR, 'div[class="contact-item_card__2SOIM"]')
        qty_before = len(contacts_before)
        print(f"Contacts before deletion: {qty_before}")
        return qty_before

    def countContactsAfter(self):
        contacts_after = self.driver.find_elements(By.CSS_SELECTOR, 'div[class="contact-item_card__2SOIM"]')
        qty_after = len(contacts_after)
        print(f"Contacts after deletion: {qty_after}")
        return qty_after

    def isContactWasDeleted(self, qty_before):
        qty_after = self.countContactsAfter()  # Get the count after
        assert qty_before - 1 == qty_after, f"Expected {qty_before - 1}, but got {qty_after}"
        print("Contact was successfully deleted.")








