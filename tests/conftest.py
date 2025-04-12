import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.implicitly_wait(3)

    yield driver

    driver.quit()

@pytest.fixture()
def login(driver):
    driver.get('https://telranedu.web.app/home')
    clickLoginBtn=driver.find_element(By.CSS_SELECTOR, '[href="/login"]')
    clickLoginBtn.click()
    email=driver.find_element(By.NAME, 'email')
    email.click()
    email.send_keys('kashamasha@gmail.com')
    pwd = driver.find_element(By.NAME, 'password')
    pwd.click()
    pwd.send_keys('QwertyQwerty1!')
    time.sleep(2)
    pressLogin=driver.find_element(By.NAME, 'login')
    pressLogin.click()
    return driver

@pytest.fixture()
def addContact(driver,login):
    clickAddLink=driver.find_element(By.CSS_SELECTOR, '[href="/add"]')
    clickAddLink.click()

    nameField=driver.find_element(By.CSS_SELECTOR, 'input:nth-child(1)')
    nameField.click()
    nameField.send_keys('Pasha')

    lastNameField = driver.find_element(By.CSS_SELECTOR, 'input:nth-child(2)')
    lastNameField.click()
    lastNameField.send_keys('Dow')

    phoneField = driver.find_element(By.CSS_SELECTOR, 'input:nth-child(3)')
    phoneField.click()
    phoneField.send_keys('12345678920')

    emailField = driver.find_element(By.CSS_SELECTOR, 'input:nth-child(4)')
    emailField.click()
    emailField.send_keys('qwerty@gmail.com')

    addressField = driver.find_element(By.CSS_SELECTOR, 'input:nth-child(5)')
    addressField.click()
    addressField.send_keys('Haifa')

    descriptionField = driver.find_element(By.CSS_SELECTOR, 'input:nth-child(6)')
    descriptionField.click()
    descriptionField.send_keys('QA')

    clickSaveBtn = driver.find_element(By.CSS_SELECTOR, '.add_form__2rsm2 button')
    clickSaveBtn.click()

    return login




    #driver.quit()

