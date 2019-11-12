from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from getpass import getpass
from course4tk4 import Ce4tk4
from courseMain import Course
import time


driver = webdriver.Chrome(executable_path='/Users/murtmac/Documents/studymode/chromedriver')

main = Ce4tk4(driver)
main.browser()

while(True):
    command = input("Type Command to run: ")
    if command == "getState":
        main.getState()
    elif command == "exportState":
        main.exportState()
    elif command == "quit":
        main.driver.quit()
        break
    else:
        continue

    time.sleep(10)




# start = loginflow(username,password)

# driver.execute_script("window.open('','_blank');")

# start.driver.quit()




