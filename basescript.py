from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from getpass import getpass
from course4tk4 import Ce4tk4
from course4tl4 import Ce4tl4
from course4dk4 import Ce4dk4
from course4ek4 import Ce4ek4
from courseMain import Course
import time
import PySimpleGUI as sg


driver = webdriver.Chrome(executable_path='/Users/murtmac/Documents/studymode/chromedriver')

def lookupFunction(driver):
    dispatch_dictionary = {'LoadState':Ce4tk4(driver).loadSpecificState, 'SaveState':Ce4tk4(driver).exportSpecificState, 'NewState':Ce4tk4(driver).browser, 'MongoUpload':Ce4tk4(driver).mongoSpecificUpload, 'MongoLoad': Ce4tk4(driver).mongoSpecificLoad,
                        'LoadState0':Ce4tl4(driver).loadSpecificState, 'SaveState1':Ce4tl4(driver).exportSpecificState, 'NewState2':Ce4tl4(driver).browser, 'MongoUpload3':Ce4tl4(driver).mongoSpecificUpload, 'MongoLoad4': Ce4tl4(driver).mongoSpecificLoad,
                        'LoadState5':Ce4dk4(driver).loadSpecificState, 'SaveState6':Ce4dk4(driver).exportSpecificState, 'NewState7':Ce4dk4(driver).browser, 'MongoUpload8':Ce4dk4(driver).mongoSpecificUpload, 'MongoLoad9': Ce4dk4(driver).mongoSpecificLoad,
                        'LoadState10':Ce4ek4(driver).loadSpecificState, 'SaveState11':Ce4ek4(driver).exportSpecificState, 'NewState12':Ce4ek4(driver).browser, 'MongoUpload13':Ce4ek4(driver).mongoSpecificUpload, 'MongoLoad14': Ce4ek4(driver).mongoSpecificLoad}
    return dispatch_dictionary

# Layout the design of the GUI
layout = [[sg.Text('Please click a button', auto_size_text=True),sg.Quit(focus=True), sg.Button('New')],
          [sg.Text('4TK4')],
          [sg.Button('LoadState'), sg.Button('SaveState'), sg.Button('NewState'), sg.Button('MongoUpload'), sg.Button('MongoLoad')],
          [sg.Text('_'*60)],[sg.Text('4TL4')],
          [sg.Button('LoadState'), sg.Button('SaveState'), sg.Button('NewState'), sg.Button('MongoUpload'), sg.Button('MongoLoad')],
          [sg.Text('_'*60)],[sg.Text('4DK4')],
          [sg.Button('LoadState'), sg.Button('SaveState'), sg.Button('NewState'), sg.Button('MongoUpload'), sg.Button('MongoLoad')],
          [sg.Text('_'*60)],[sg.Text('4EK4')],
          [sg.Button('LoadState'), sg.Button('SaveState'), sg.Button('NewState'), sg.Button('MongoUpload'), sg.Button('MongoLoad')]]

# Show the Window to the user
window = sg.Window('StudyMode App', layout)

# Event loop. Read buttons, make callbacks
while True:
    # Read the Window
    event, value = window.read()
    if event in ('Quit', None):
        driver.quit()
        break
    if event in ('New', None):
        driver.quit()
        driver = webdriver.Chrome(executable_path='/Users/murtmac/Documents/studymode/chromedriver')
        continue
    # Lookup event in function dictionary
    if event in lookupFunction(driver):
        func_to_call = lookupFunction(driver)[event]   # get function from dispatch dictionary
        func_to_call()
    else:
        print('Event {} not in dispatch dictionary'.format(event))

window.close()



