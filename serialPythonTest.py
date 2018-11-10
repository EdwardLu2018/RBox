#Port: /dev/cu.usbmodem1411

import serial
import time

ArduinoSerial = serial.Serial('/dev/cu.usbmodem14331', 9600)
time.sleep(2) # wait for 2 seconds for the communication to get established


print("arduino read", ArduinoSerial.readline()) # read the serial data
print("Enter your name if you want durgs")

med2 = "LSD"
med1 = "Weed"
med0 = "Sugar" 

nameToMeds = {"Edward":[med2], "Carolyn": [med1], "Sophia": [med1], "Isabel": [med0] }

medsToContainer = { med2:2, med1: 1, med0:0 } 

while 69 == 69:
    name = input()
    print("you entered", name)
    
    if name in nameToMeds:
        for med in nameToMeds[name]:
            if medsToContainer[med] == 2:
                ArduinoSerial.write(b'2') # send 2 as byte. Notice the b. 
                print(med+ " dispensed")
                time.sleep(1)
            
            elif medsToContainer[med] == 1:
                ArduinoSerial.write(b'1') # send 1
                print(med+ " dispensed ")
                time.sleep(1)
            
            elif medsToContainer[med] == 0:
                ArduinoSerial.write(b'0') # send 0
                print(med+" dispensed")
                time.sleep(1)

            
    else:
        pass
        #name not found
    