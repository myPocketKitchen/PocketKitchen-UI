

from picamera import PiCamera
from time import sleep
import datetime
import keyboard

#camera.start_preview()

camera = PiCamera()

print("Food Type: ")
food_type = input()

print("State: ")
state = input()

while True: 
    try:
        pass
    except KeyboardInterrupt:
        print("interrupt")
        stamp = '{}{}'.format(state, datetime.datetime.now())
        camera.capture('/home/pi/food_images/{}/{}.jpg'.format(food_type, stamp))
        # camera.stop_preview()