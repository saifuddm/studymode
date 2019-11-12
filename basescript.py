from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from getpass import getpass
from course4tk4 import Ce4tk4
from courseMain import Course
import time
import PySimpleGUI as sg


driver = webdriver.Chrome(executable_path='/Users/murtmac/Documents/studymode/chromedriver')

main = Ce4tk4(driver)


# while(True):
#     command = input("Type Command to run: ")
#     if command == "getState":
#         main.getState()
#     elif command == "exportState":
#         main.exportState()
#     elif command == "newState":
#         main.browser()
#     elif command == "loadState":
#         main.loadState()
#     elif command == "quit":
#         main.driver.quit()
#         break
#     else:
#         continue

#     time.sleep(10)



# Lookup dictionary that maps button to function to call
dispatch_dictionary = {'LoadState':main.loadState, 'SaveState':main.exportState, 'NewState':main.browser}
# Layout the design of the GUI
layout = [[sg.Text('Please click a button', auto_size_text=True)],
          [sg.Button('LoadState'), sg.Button('SaveState'), sg.Button('NewState'), sg.Quit(focus=True)]]

# Show the Window to the user
window = sg.Window('StudyMode App', layout)

# Event loop. Read buttons, make callbacks
while True:
    # Read the Window
    event, value = window.read()
    if event in ('Quit', None):
        main.driver.quit()
        break
    # Lookup event in function dictionary
    if event in dispatch_dictionary:
        func_to_call = dispatch_dictionary[event]   # get function from dispatch dictionary
        func_to_call()
    else:
        print('Event {} not in dispatch dictionary'.format(event))

window.close()

    # All done!
sg.popup_ok('Good Job')



