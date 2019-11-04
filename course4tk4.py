from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from courseMain import Course

class Ce4tk4(Course):
    def __init__(self,userId,passId,chrome):
        self.driver = chrome
        super().__init__(userId,passId,self.driver)
        self.baselinks = ['https://www.ece.mcmaster.ca/~jkzhang/4TK4_Course_digital%20communications.pdf']
        
        
    def test(self):
        print("test")

    def browser(self):
        super().login()
        super().newTab()
        for i in self.baselinks:
            self.driver.get(i)
            self.driver.implicitly_wait(10)

        
        
        
