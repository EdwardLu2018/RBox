from selenium import webdriver
import time
import json

driver = webdriver.Chrome("/Users/Edward/Documents/chromedriver")
 
url='https://edwardlu2018.github.io/RBox/'
driver.get(url)
scriptArray="""return Array.apply(0, new Array(localStorage.length)).map(function (o, i) { return localStorage.getItem(localStorage.key(i)); })""" 

while 1:
    result = driver.execute_script(scriptArray)
    print(result)
    time.sleep(1)