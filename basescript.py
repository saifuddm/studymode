from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from getpass import getpass
from course4tk4 import Ce4tk4
from courseMain import Course

username = input("Type your username: ")
password = getpass()
driver = webdriver.Chrome(executable_path='/Users/murtmac/Documents/studymode/chromedriver')

main = Ce4tk4(username,password,driver)
main.browser()




# start = loginflow(username,password)

# driver.execute_script("window.open('','_blank');")

# start.driver.quit()




