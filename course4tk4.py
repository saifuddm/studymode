from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from getpass import getpass
from courseMain import Course


class Ce4tk4(Course):
    def __init__(self,chrome):
        self.driver = chrome
        super().__init__(self.driver)
        self.baselinks = ['https://www.ece.mcmaster.ca/~jkzhang/4TK4_Course_digital%20communications.pdf']
        self.filename = "ce4tk4State.txt"
        self.name = "4TK4"

    def browser(self):
        tabnumber = 0
        # super().login(userId,passId)
        # userId = input("Type your username: ")
        # passId = getpass()
        super().loginDev()
        for i in self.baselinks:
            tabnumber = tabnumber + 1
            super().newTabAndFocus(tabnumber)
            self.driver.get(i)
            self.driver.implicitly_wait(10)

    def exportSpecificState(self):
        super().exportState(self.filename)
    
    def loadSpecificState(self):
        super().loadState(self.filename)

    def mongoSpecificUpload(self):
        super().mongoUpload(self.name)

    def mongoSpecificLoad(self):
        super().mongoLoad(self.name)






        
        
        
