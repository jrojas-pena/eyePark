from http_eyepark_client import http_eyepark_client
from plate_reader import plate_reader
import json
from datetime import datetime
import cv2
import time

#taking picture from camera
def take_picture(camera_port):
    camera = cv2.VideoCapture(camera_port)
    time.sleep(0.1) #Sleep so image is not dark
    result_value, image = camera.read() #read returns tuple of bool and another tuple
    image_path = "/tmp/eyepark%s.png"%(datetime.now().strftime("%Y%-m%-d%-H%-M%-S"))
    cv2.imwrite(image_path, image) #write image into RAM
    del(camera)
    return image_path


#configuration file
config = json.load(open('config/system_config.json'))

#parameters from config file
country = config['country']
config_file = config['config_file']
runtime_data = config['runtime_data']
camera_port = config['camera_port']

#declaring plate_reader object
reader = plate_reader(country, config_file, runtime_data)

print(reader.read_plate(take_picture))








