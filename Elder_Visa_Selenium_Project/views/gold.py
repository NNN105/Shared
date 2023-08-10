from selenium.webdriver.common.by import By

from views.home import Home
from views.externo import Externo


class Gold(Home):
    PAGE_LABEL = (By.CSS_SELECTOR, 'div.vs-mb-3.vs-container > div > h1')
    BANK_LINK = (By.CSS_SELECTOR, 'a[href="http://www.bna.com.ar"]')
       
    def check_gold_page(self):
        return self.wait_for(self.PAGE_LABEL).text
    
    def go_bank(self):
        self.find(self.BANK_LINK).click()
        return Externo(self.driver)