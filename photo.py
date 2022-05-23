

from picamera import PiCamera
from time import sleep
import datetime

camera = PiCamera()


print("Food Type: ")
food_type = input()

print("State: ")
state = input()

i = 1

while True: 
    camera.start_preview()
    # camera.annotate_text = 'Waiting...'
    print("Trigger")
    trigger = input()
    if trigger == "":
        # camera.annotate_text =
        print("interrupt")
        # stamp = '{}{}'.format(state, datetime.datetime.now())
        name = food_type + str(i) 
        i += 1
        camera.capture('/home/pi/new_images/{}/{}.jpg'.format(food_type, name))
    else:
        pass
        

camera.stop_preview()