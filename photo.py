

from picamera import PiCamera
from time import sleep
import datetime

#camera.start_preview()

camera = PiCamera()

print("Food Type: ")
food_type = input()

print("State: ")
state = input()

for i in range(5):
    stamp = '{}{}'.format(state, datetime.datetime.now())
    camera.capture('/home/pi/food_images/food_type/{}.jpg'.format(stamp))


# camera.stop_preview()




