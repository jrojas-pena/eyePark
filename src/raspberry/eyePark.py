from http_eyepark_client import http_eyepark_client
from plate_reader import plate_reader
from gpiozero import DistanceSensor, LED
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

def get_keypad_input():
    return "123"

def get_distance():
    dist.sleep
    return 

def display_lcd(message):
    lcd_i2c.lcd_init()
    lcd_i2c.lcd_string()
    return




#configuration file
config = json.load(open('config/system_config.json'))

#parameters from config file
country = config['country']
config_file = config['config_file']
runtime_data = config['runtime_data']
camera_port = config['camera_port']

reader = plate_reader(country, config_file, runtime_data)
client = http_eyepark_client(config)

while True:
    image_path = take_picture(camera_port)
    read = reader.read_plate(image_path)

    print(read)

    #remove files from RAM
    os.remove(image_path)
    if read == "CASZ203":
        break
    
#declaring http_eyepark_client
client = http_eyepark_client(config)










