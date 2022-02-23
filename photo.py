

from picamera import PiCamera
from time import sleep
import datetime

#camera.start_preview()

camera = PiCamera()

for i in range(5):
    sleep(3)
    timestamp = '{}'.format(datetime.datetime.now())
    camera.capture('/home/pi/food-cam/images/{}.jpg'.format(timestamp))


# camera.stop_preview()




