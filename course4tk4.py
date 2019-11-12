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

    def getState(self):
        state = self.driver.wiclndow_handles
        print(state)
        currentState = []
        for window in range(len(state)):
            super().newTabAndFocus(window)
            urls = self.driver.current_url
            currentState.append(urls)
        
        return currentState

    def exportState(self):
        currentState = self.getState()
        exportstate = open("exportState.txt","w+")
        for tabs in currentState:
            exportstate.write(tabs + '\n')
        
        exportstate.close()

    def loadState(self):
        previousState = open("exportState.txt",'r')
        previousStateLinks = []
        for tabs in previousState:
            previousStateLinks.append(tabs)

        super().loginDev()
         # From one to ignore the main login page
        for i in range(1,len(previousStateLinks)):
            super().newTabAndFocus(i)
            self.driver.get(previousStateLinks[i])
        




        
        
        
