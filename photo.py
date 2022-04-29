

from picamera import PiCamera
from time import sleep
import datetime

camera = PiCamera()


print("Food Type: ")
food_type = input()

print("State: ")
state = input()

i = 0

while True: 
    camera.start_preview()
    print("Trigger")
    trigger = input()
    
    if trigger == "":
        i += 1
        camera.annotate_text = 'Trigger %' % (i)
        print("interrupt")
        stamp = '{}{}'.format(state, datetime.datetime.now())
        camera.capture('/home/pi/food_images/{}/{}.jpg'.format(food_type, stamp))
    else:
        pass
        


camera.stop_preview()