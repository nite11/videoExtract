#used code from 
# https://www.geeksforgeeks.org/get-all-text-of-the-page-using-selenium-in-python/
# https://stackoverflow.com/questions/23270175/google-reverse-image-search-using-post-request

# Importing necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import os

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

f = open("frameInfo.txt", "w")
f.write('')
f.close()


tags=['cnc','soldering']

for file in os.listdir("framesTest"): 
    filePath = 'framesTest\\'+file
    searchUrl = 'http://www.google.com/searchbyimage/upload'
    multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
    response = requests.post(searchUrl, files=multipart, allow_redirects=False)
    fetchUrl = response.headers['Location']

    driver = webdriver.Chrome(options=options)
    # Target URL
    #print(fetchUrl)
    driver.get(fetchUrl)
    #time.sleep(1)
    driver.find_element(By.ID,'W0wltc').click()   #button id="W0wltc" to reject the cookies
    #time.sleep(1)
    driver.find_element(By.CLASS_NAME,'iJ1Kvb').click()  #<div class="iJ1Kvb"> to click on 'similar images'
    # To load entire webpage
    #time.sleep(1)

    # Printing the whole body text
    text=driver.find_element(By.XPATH, "/html/body").text.lower()
    for tag in tags:
        if text.find(' '+tag+' ') !=-1:
            f = open("frameInfo.txt", "a")
            f.write(f"{file},{tag}\n")
            f.close()
            

    # Closing the driver
    driver.close()


