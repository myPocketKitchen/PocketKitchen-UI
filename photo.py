

from picamera import PiCamera
from time import sleep
import datetime

#camera.start_preview()


for i in range(5):
    sleep(3)
    timestamp = '{}'.format(datetime.datetime.now())
    camera.capture('/home/pi/images/{}.jpg'.format(timestamp))


# camera.stop_preview()




