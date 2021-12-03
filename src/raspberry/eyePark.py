from http_eyepark_client import http_eyepark_client
from plate_reader import plate_reader
from gpiozero import DistanceSensor, LED
from keypad import KeyPad
import json
from datetime import datetime
import cv2
import time
import os
import lcd_i2c


#taking picture from camera
def take_picture(camera_port):
    camera = cv2.VideoCapture(camera_port)
    time.sleep(0.1) #Sleep so image is not dark
    result_value, image = camera.read() #read returns tuple of bool and another tuple
    image_path = "/tmp/eyepark%s.png"%(datetime.now().strftime("%Y%-m%-d%-H%-M%-S"))
    cv2.imwrite(image_path, image) #write image into RAM
    del(camera)
    return image_path

def plate_was_not_found(keypad, data, client):
    pin_attemps = 0
    LED_RED.on()
    input = ""
    lcd_i2c.lcd_string("Accept %s?"%data['license-plate'], lcd_i2c.LCD_LINE_1)
    lcd_i2c.lcd_string("Enter PIN:", lcd_i2c.LCD_LINE_2)
    start = datetime.now()
    while pin_attemps < 3 and (datetime.now() - start).seconds < 30:
        pressed = keypad.readKey()
        if pressed != "A" and pressed is not None:
            print(pressed)
            input += pressed
        elif pressed == "A":
            if input == "1234" and client.addPlateNumber(data):
                lcd_i2c.lcd_string("%s accepted"%data['license-plate'], lcd_i2c.LCD_LINE_1)
                lcd_i2c.lcd_string("", lcd_i2c.LCD_LINE_2)
                LED_RED.off()
                LED_GREEN.on()
                time.sleep(10) #Green LED on for 10 seconds
                LED_GREEN.off()                
                break
            else:
                input = "" # Reset input if password is wrong
                pin_attemps += 1

        lcd_i2c.lcd_string("Enter PIN: %s"%(len(input)*"*"), lcd_i2c.LCD_LINE_2)

    while not client.alertSecurity(data): # Loop until response from server is True, 1 second wait in between
        lcd_i2c.lcd_string("%s rejected"%data['license-plate'], lcd_i2c.LCD_LINE_1)
        lcd_i2c.lcd_string("Calling security", lcd_i2c.LCD_LINE_2)
        time.sleep(1)
    LED_RED.off()




#configuration file
config = json.load(open('config/system_config.json'))

#parameters from config file
country = config['country']
config_file = config['config_file']
runtime_data = config['runtime_data']
camera_port = config['camera_port']

reader = plate_reader(country, config_file, runtime_data)
client = http_eyepark_client(config)

# Initialize hardware
LED_GREEN = LED(18) #Green LED connected to GPIO18
LED_RED = LED(24)   #Red LED connected to GPIO24
lcd_i2c.lcd_init() # Initialize LCD panel
ultrasonic = DistanceSensor(echo=23, trigger=25, threshold_distance=0.3) # Initialize ultrasonic distance sensor
isCarInDb = False
keypad = KeyPad()


numberOfTries = 0

while True:
    numberOfTries += 1
    ultrasonic.wait_for_in_range() #Loop starts when car is at 30cm or less
    image_path = take_picture(camera_port)
    plate = reader.read_plate(image_path)

    print(plate)
    data = {
        "parking-lot-number": 52,
        "license-plate": plate
    }
    isCarInDb = client.checkPlateNumber(data)

    #remove files from RAM
    os.remove(image_path)
    if isCarInDb and numberOfTries < 10 and plate:
        LED_GREEN.on()
        time.sleep(10) #Green LED on for 10 seconds
        LED_GREEN.off()
        ultrasonic.wait_for_out_of_range() #Loop stops until car is at a distance of 30cm or more
        numberOfTries = 0 #Reset number of tries
    elif numberOfTries > 10 and plate: # If number of tries of reading the license plate is more than 10
        plate_was_not_found(keypad, data, client)
        ultrasonic.wait_for_out_of_range() #Loop stops until car is at a distance of 30cm or more
        numberOfTries = 0












