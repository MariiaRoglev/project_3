import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
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






    #driver.get('https://telranedu.web.app/home')

    # all that connects to Valid Login
    #clickLoginBtn = driver.find_element(By.CSS_SELECTOR, '[href="/login"]')
    #clickLoginBtn.click()
    #email = driver.find_element(By.NAME, 'email')
    #email.click()
    #email.send_keys('kashamasha@gmail.com')
    #pwd = driver.find_element(By.NAME, 'password')
    #pwd.click()
    #pwd.send_keys('QwertyQwerty1!')
    #time.sleep(5)
    #pressLogin = driver.find_element(By.NAME, 'login')
    #pressLogin.click()



    #driver.close()