from selenium import webdriver
import time
import json
import serial

ArduinoSerial = serial.Serial('/dev/cu.usbmodem1411', 9600)
time.sleep(2) # wait for 2 seconds for the communication to get established

driver = webdriver.Chrome("/Users/Edward/Documents/chromedriver")

url='https://edwardlu2018.github.io/RBox/'
driver.get(url)
scriptArray="""return Array.apply(0, new Array(localStorage.length)).map(function (o, i) { return localStorage.getItem(localStorage.key(i)); })""" 

while 1:
    result = driver.execute_script(scriptArray)
    dictStr = result[0]
    currCust = ""
    if len(result) == 2:
        dictStr = result[1]
    if len(result) == 3:
        dictStr = result[2]
        currCust = result[0]
    json_acceptable_string = dictStr.replace("'", "\"")
    patientDict = json.loads(json_acceptable_string)
    time.sleep(1)
    if currCust != "":
        name = currCust
        if currCust in patientDict:
            print(patientDict[name])
            for i in range(len(patientDict[name])-1):
                if i == 2 and int(patientDict[name][i]) != 0:
                    ArduinoSerial.write(b'2') # send 2 as byte. Notice the b. 
                    print("MedA dispensed")
                    time.sleep(1)
                
                elif i == 1 and int(patientDict[name][i]) != 0:
                    ArduinoSerial.write(b'1') # send 1
                    print("MedB dispensed ")
                    time.sleep(1)
                
                elif i == 0 and int(patientDict[name][i]) != 0:
                    ArduinoSerial.write(b'0') # send 0
                    print("MedC dispensed")
                    time.sleep(1)
    currCust = ""

