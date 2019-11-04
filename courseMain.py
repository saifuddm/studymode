from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

class Course():
    def __init__(self,userId,passId,chrome):
        self.userId = userId
        self.passId = passId
        self.driver = chrome

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

    def newTab(self):
        self.driver.execute_script("window.open('','_blank');")

    def newTabAndFocus(self):
        self.newTab()


    def waitTime(self,amount):
        WebDriverWait(self.driver,amount)