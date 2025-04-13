from selenium.webdriver.common.by import By


class loginForm:

    def __init__(self,driver):#self==page.We saved browser for our page. need to add to all classed (pages)
        self.driver=driver

    def fillLoginForm(self):
        email = self.driver.find_element(By.NAME, 'email')
        email.click()
        email.send_keys('kashamasha@gmail.com')
        pwd = self.driver.find_element(By.NAME, 'password')
        pwd.click()
        pwd.send_keys('QwertyQwerty1!')

    def fillLoginFormWithEmptyEmail(self):
        email = self.driver.find_element(By.NAME, 'email')
        email.click()
        email.send_keys('')
        pwd = self.driver.find_element(By.NAME, 'password')
        pwd.click()
        pwd.send_keys('QwertyQwerty1!')


    def clickLogin(self):
        pressLogin = self.driver.find_element(By.NAME, 'login')
        pressLogin.click()