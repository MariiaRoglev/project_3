from selenium.webdriver.common.by import By
from needconftest import driver

class homePage:

    def __init__(self,driver):#self==page.We saved browser for our page. need to add to all classed (pages)
        self.driver=driver


    def openSite(self):#to open Link. Take browser from previous initiation
        self.driver.get('https://telranedu.web.app/home')


    def clickLoginBtn(self):
        clickLoginBtn = self.driver.find_element(By.CSS_SELECTOR, '[href="/login"]')
        clickLoginBtn.click()

    def checkLoginSuccess(self,qty):
        signOutbtn = self.driver.find_elements(By.XPATH, '//button[.="Sign Out"]')
        assert len(signOutbtn) == qty  # if element=1 like present

    def clickContactBtn(self):
        clickContactsBtn=self.driver.find_element(By.CSS_SELECTOR, '[href="/add"]')
        clickContactsBtn.click()