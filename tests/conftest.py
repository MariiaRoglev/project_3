import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import logging

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

#-----------------------#FOR SCREENSHOT AND LOGS!!!!!!!!!-----------------------------------------
def capture_screenshot(test_name):
    try:
        folder_path = "C:/Users/winte/PycharmProjects/PythonProject3/tests/screenshot"
        screenshot_path = os.path.join(folder_path, f"{test_name}_failed.png")
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")
        return screenshot_path
    except Exception as e:
        print(f"Error capturing screenshot: {e}")
        return None

def pytest_configure(config):
    logging.basicConfig(
        filename="test_results.log",
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
    )
    logging.info("Starting Test Session")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Log the test result
    if report.when == "call":  # Only handle the test call stage
        test_name = item.name

        if report.passed:
            logging.info(f"PASSED: {test_name}")
        elif report.failed:
            # Capture a screenshot if the test failed
            screenshot_path = capture_screenshot(test_name)

            # Log the failure and screenshot path
            if screenshot_path:
                logging.error(f"FAILED: {test_name} (Screenshot: {screenshot_path})")
            else:
                logging.error(f"FAILED: {test_name} (Screenshot capture failed)")
        else:
            logging.warning(f"SKIPPED: {test_name}")










