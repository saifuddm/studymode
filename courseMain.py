from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

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

    def waitTime(self,amount):
        WebDriverWait(self.driver,amount)