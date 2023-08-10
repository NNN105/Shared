from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Home(object):  

    def __init__(self,myDriver):
        self.driver = myDriver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find(self, locator):
        return self.driver.find_element(*locator)
    
    HEADER_ITEM = (By.ID,"vs-navigation-header")
    def verify_header(self):
        self.driver.get("https://www.visa.com.ar/")
        return self.wait_for(self.HEADER_ITEM)

        
    PERSONA_ITEM = (By.CSS_SELECTOR,"#vs-lowernav > ul.vs-lowernav-list > li:nth-child(1) > a")
    CREDITO_ITEM = (By.CSS_SELECTOR,"#vs-submenu-list-0-0-0 > li:nth-child(2) > a")
    def go_credict(self):
        from views.credict import Credict
        ActionChains(self.driver).move_to_element(self.find(self.PERSONA_ITEM)).perform()
        self.find(self.CREDITO_ITEM).click()
        return Credict(self.driver)
        