

from picamera import PiCamera
from time import sleep
import datetime

camera = PiCamera()
camera.start_preview()

print("Food Type: ")
food_type = input()

print("State: ")
state = input()

while True: 
    print("Trigger")
    trigger = input()

    if trigger == "":
        print("interrupt")
        stamp = '{}{}'.format(state, datetime.datetime.now())
        camera.capture('/home/pi/food_images/{}/{}.jpg'.format(food_type, stamp))
    else:
        pass
        


camera.stop_preview()