from selenium.webdriver.common.by import By

from views.home import Home


class Externo(Home):
    PAGE_LABEL = (By.CSS_SELECTOR, 'div.vs-mb-3.vs-container > div > h1')
   
    def check_external_title(self):
        self.driver.implicitly_wait(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        title = self.driver.title
        self.driver.close()
        return title
    