from selenium.webdriver.common.by import By

from views.home import Home
from views.classic import Classic
from views.gold import Gold
from views.platinum import Platinum
from views.signature import Signature

class Credict(Home):
    PAGE_LABEL = (By.CSS_SELECTOR, 'div.vs-mb-3.vs-container > div > h1')
    CLASSIC_LINK = (By.CSS_SELECTOR,'a[href="/tu-visa/obtene-tu-tarjeta/credito-classic.html"]')
    GOLD_LINK = (By.CSS_SELECTOR,'a[href="/tu-visa/obtene-tu-tarjeta/visa-gold.html"]')
    PLATINUM_LINK = (By.CSS_SELECTOR,'a[href="/tu-visa/obtene-tu-tarjeta/visa-platinum.html"]')
    SIGNATURE_LINK = (By.CSS_SELECTOR,'a[href="/tu-visa/obtene-tu-tarjeta/credito-signature.html"]')
             
    def check_credict_page(self):
        return self.wait_for(self.PAGE_LABEL).text

    def go_classic(self):
        self.find(self.CLASSIC_LINK).click()
        return Classic(self.driver)

    def go_gold(self):
        self.find(self.GOLD_LINK).click()
        return Gold(self.driver)
    
    def go_platinum(self):
        self.find(self.PLATINUM_LINK).click()
        return Platinum(self.driver)
    
    def go_signature(self):
        self.find(self.SIGNATURE_LINK).click()
        return Signature(self.driver)