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


# Lookup dictionary that maps button to function to call
dispatch_dictionary = {'LoadState':Ce4tk4(driver).loadSpecificState, 'SaveState':Ce4tk4(driver).exportSpecificState, 'NewState':Ce4tk4(driver).browser, 'MongoUpload':Ce4tk4(driver).mongoSpecificUpload,
                        'LoadState0':Ce4tl4(driver).loadSpecificState, 'SaveState1':Ce4tl4(driver).exportSpecificState, 'NewState2':Ce4tl4(driver).browser,
                        'LoadState3':Ce4dk4(driver).loadSpecificState, 'SaveState4':Ce4dk4(driver).exportSpecificState, 'NewState5':Ce4dk4(driver).browser,
                        'LoadState6':Ce4ek4(driver).loadSpecificState, 'SaveState7':Ce4ek4(driver).exportSpecificState, 'NewState8':Ce4ek4(driver).browser,}

# Layout the design of the GUI
layout = [[sg.Text('Please click a button', auto_size_text=True),sg.Quit(focus=True)],
          [sg.Text('4TK4')],
          [sg.Button('LoadState'), sg.Button('SaveState'), sg.Button('NewState'), sg.Button('MongoUpload')],
          [sg.Text('_'*30)],[sg.Text('4TL4')],
          [sg.Button('LoadState'), sg.Button('SaveState'), sg.Button('NewState')],
          [sg.Text('_'*30)],[sg.Text('4DK4')],
          [sg.Button('LoadState'), sg.Button('SaveState'), sg.Button('NewState')],
          [sg.Text('_'*30)],[sg.Text('4EK4')],
          [sg.Button('LoadState'), sg.Button('SaveState'), sg.Button('NewState')]]

# Show the Window to the user
window = sg.Window('StudyMode App', layout)

# Event loop. Read buttons, make callbacks
while True:
    # Read the Window
    event, value = window.read()
    if event in ('Quit', None):
        driver.quit()
        break
    # Lookup event in function dictionary
    if event in dispatch_dictionary:
        func_to_call = dispatch_dictionary[event]   # get function from dispatch dictionary
        func_to_call()
    else:
        print('Event {} not in dispatch dictionary'.format(event))

window.close()



