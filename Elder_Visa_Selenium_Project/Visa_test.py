'''
Created on 9 ago. 2023

@author: Nico
'''
import unittest
from pyunitreport import HTMLTestRunner

from selenium import webdriver
from views.home import *

class Visa(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        driver = cls.driver
        driver.get("https://www.visa.com.ar/")
        cls.home = Home(driver)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element(By.CSS_SELECTOR,"#CookieReportsBanner > div.wscrBannerContent > div.wscrBannerContentInner > a.wscrOk").click()


    def test_01_Personas_Obtener_Tarjeta_Credito_Classic(self):
        # Add first product
        self.home.verify_header()
        self.credict = self.home.go_credict()
        self.assertEqual(self.credict.check_credict_page(),"Tarjetas Visa Crédito")
        self.classic = self.credict.go_classic()
        self.assertEqual(self.classic.check_classic_page(),"Visa Classic Crédito")
        self.bank = self.classic.go_bank()
        self.assertEqual(self.bank.check_external_title(),"Banco de la Nación Argentina")
        self.driver.switch_to.window(self.driver.window_handles[0])

    def test_02_Personas_Obtener_Tarjeta_Credito_Gold(self):
        # Add first product
        self.home.verify_header()
        self.credict = self.home.go_credict()
        self.assertEqual(self.credict.check_credict_page(),"Tarjetas Visa Crédito")
        self.gold = self.credict.go_gold()
        self.assertEqual(self.gold.check_gold_page(),"Visa Gold Crédito")
        self.bank = self.gold.go_bank()
        self.assertEqual(self.bank.check_external_title(),"Banco de la Nación Argentina")
        self.driver.switch_to.window(self.driver.window_handles[0])  
        
    def test_03_Personas_Obtener_Tarjeta_Credito_Platinum(self):
        # Add first product
        self.home.verify_header()
        self.credict = self.home.go_credict()
        self.assertEqual(self.credict.check_credict_page(),"Tarjetas Visa Crédito")
        self.platinum = self.credict.go_platinum()
        self.assertEqual(self.platinum.check_platinum_page(),"Visa Platinum Crédito")
        self.bank = self.platinum.go_bank()
        self.assertEqual(self.bank.check_external_title(),"Banco de la Nación Argentina")
        self.driver.switch_to.window(self.driver.window_handles[0])         
        
    def test_04_Personas_Obtener_Tarjeta_Credito_Signature(self):
        # Add first product
        self.home.verify_header()
        self.credict = self.home.go_credict()
        self.assertEqual(self.credict.check_credict_page(),"Tarjetas Visa Crédito")
        self.signature = self.credict.go_signature()
        self.assertEqual(self.signature.check_signature_page(),"Visa Signature Crédito")
        self.bank = self.signature.go_bank()
        self.assertEqual(self.bank.check_external_title(),"Banco de la Nación Argentina")
        self.driver.switch_to.window(self.driver.window_handles[0])   
           
    @classmethod     
    def tearDownClass(cls):
        cls.driver.quit()
            
                   
if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'Visa-report'))

