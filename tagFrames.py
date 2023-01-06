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
options.add_experimental_option('excludeSwitches', ['enable-logging']) #to disable some useless console messages

f = open("frameInfo.txt", "w")
f.write('')
f.close()


tags=['cnc','soldering']  #input tags

#to post HTTP request to Google Image Search with the image file
for file in os.listdir("framesTest"):  #have used 'framesTest' for testing with a few frames. 
                                        # to run with all the 'frames' replace with frames
    filePath = 'framesTest\\'+file
    searchUrl = 'http://www.google.com/searchbyimage/upload'
    multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
    response = requests.post(searchUrl, files=multipart, allow_redirects=False)
    fetchUrl = response.headers['Location']

    driver = webdriver.Chrome(options=options)
    
    driver.get(fetchUrl)
    #time.sleep(1), sleep may be required to wait for the webpages to load entirely

    #every time the program opens the URL, Google first displays the Accept/Reject cookies message
    try:
        driver.find_element(By.ID,'W0wltc').click()   #button id="W0wltc" to reject the cookies
    except:
        pass
    
    driver.find_element(By.CLASS_NAME,'iJ1Kvb').click()  #<div class="iJ1Kvb"> to click on 'similar images'
    
    #time.sleep(1)

    #gather all the text on the resulting webpage
    text=driver.find_element(By.XPATH, "/html/body").text.lower()
    for tag in tags:
        if text.find(' '+tag+' ') !=-1:
            f = open("frameInfo.txt", "a")
            f.write(f"{file},{tag}\n")
            f.close()            

    # Closing the driver
    driver.close()