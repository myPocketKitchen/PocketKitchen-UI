

from picamera import PiCamera
from time import sleep
import datetime

#camera.start_preview()

camera = PiCamera()

food_type = input()

for i in range(5):
    sleep(3)
    stamp = '{}{}'.format(food_type,datetime.datetime.now())
    camera.capture('/home/pi/food_images/{}.jpg'.format(stamp))


# camera.stop_preview()




