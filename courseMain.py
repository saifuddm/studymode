from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import pymongo
from pymongo import MongoClient
import yaml

class Course():
    def __init__(self,chrome):
        self.driver = chrome
        self.parameterLoad()

    def login(self):
        driver = self.driver
        userId = self.userId
        passId = self.passId
        driver.get('https://avenue.mcmaster.ca/?target=%2fd2l%2fhome')
        driver.implicitly_wait(10)
        login = driver.find_element_by_id("login_button")
        driver.implicitly_wait(10)
        login.click()
        user = driver.find_element_by_id("user_id")
        user.clear
        user.send_keys(userId)

        pin = driver.find_element_by_id("pin")
        pin.clear
        pin.send_keys(passId)

        submit = driver.find_element_by_id("submit")
        submit.click()
        driver.implicitly_wait(30)
    
    def loginDev(self):
        driver = self.driver
        driver.get('https://avenue.mcmaster.ca/?target=%2fd2l%2fhome')

    def newTab(self):
        self.driver.execute_script("window.open('','_blank');")

    def newTabAndFocus(self,tabnumber):
        self.newTab()
        self.driver.switch_to.window(self.driver.window_handles[tabnumber])
    
    def focusTab(self,tabnumber):
        self.driver.switch_to.window(self.driver.window_handles[tabnumber])

    def waitTime(self,amount):
        WebDriverWait(self.driver,amount)

    def getState(self):
        state = self.driver.window_handles
        currentState = []
        for window in range(len(state)):
            self.focusTab(window)
            urls = self.driver.current_url
            currentState.append(urls)
        return currentState

    def exportState(self,filename):
        currentState = self.getState()
        exportstate = open(filename,"w+")
        for tabs in currentState:
            exportstate.write(tabs + '\n')
        
        exportstate.close()

    def loadState(self,filename):
        previousState = open(filename,'r')
        previousStateLinks = []
        for tabs in previousState:
            previousStateLinks.append(tabs)

        self.loginDev()
         # From one to ignore the main login page
        for i in range(1,len(previousStateLinks)):
            self.newTabAndFocus(i)
            self.driver.get(previousStateLinks[i])
    
    def mongoUpload(self,name):
        self.mongoConnect()
        self.mongoClear(name)
        posts = []
        currentState = self.getState()
        print(len(currentState))
        for i in range(len(currentState)):
            # INTRESTINGFACT:
            # appending a dict into a list creates a refrence
            posts.append({"_id": name + str(i), "name": name, "link": currentState[i]})
        
        self.collection.insert_many(posts)

    def mongoClear(self,name):
        self.collection.delete_many({"name": name})

    def mongoLoad(self,name):
        self.mongoConnect()
        results = self.collection.find({"name":name})
        previousStateLinks = []
        for result in results:
            previousStateLinks.append(result["link"])

        self.login()
        for i in range(len(previousStateLinks)):
            self.newTabAndFocus(i)
            self.driver.get(previousStateLinks[i])

    def mongoConnect(self):
        self.cluster = MongoClient(self.mongoClient)
        self.db  = self.cluster[self.database]
        self.collection = self.db[self.collections]

    def parameterLoad(self):
        with open(r'parameters.yaml') as file:
            lists = yaml.load(file,Loader=yaml.FullLoader)

        self.mongoClient = lists['mongoClient']
        self.database = lists['db']
        self.collections = lists['collection']
        self.userId = lists['user']
        self.passId = lists['pass']