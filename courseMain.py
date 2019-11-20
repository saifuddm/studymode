from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import pymongo
from pymongo import MongoClient

class Course():
    def __init__(self,chrome):
        self.driver = chrome

    def login(self,userId,passId):
        driver = self.driver
        self.userId = self.userId
        self.passId = self.passId
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
    
    def mongoUpload(self,mongoClient,database,collections,name):
        cluster = MongoClient(mongoClient)
        db  = cluster[database]
        collection = db[collections]
        posts = []
        post = {"_id": name, "name": name, "link": ""}
        currentState = self.getState()
        for i in range(len(currentState)):
            posts.append(post)
            posts[i]["link"] = currentState[i]
        
        collection.insert_many(posts)