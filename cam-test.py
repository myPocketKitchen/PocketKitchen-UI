from picamera import PiCamera
from time import sleep


camera = PiCamera()

camera.start_preview()

key = input()

if key == 'p': 
    camera.stop_preview()