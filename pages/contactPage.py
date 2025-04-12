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


    def checkAdding(self, contact):
        card = self.driver.find_element(By.CSS_SELECTOR, '.contact-item_card__2SOIM')
        name_element = card.find_element(By.TAG_NAME, 'h2')

        actual_name = name_element.text.strip()

        assert actual_name == contact



    def scroll_to_contact(self, name):
        scrollable = self.driver.find_element(By.CSS_SELECTOR, ".contact-list-container")  # замените на реальный класс
        target = self.driver.find_element(By.XPATH, f"//h2[contains(text(), '{name}')]")

        self.driver.execute_script(
            "arguments[0].scrollTop = arguments[1].offsetTop;",
            scrollable,
            target
        )


