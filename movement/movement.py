from BirdBrain import Finch
import keyboard
import time

finch = Finch()

try:
    while True:
        if keyboard.is_pressed('up'):
            finch.set_wheels(50, 50) # forward

        elif keyboard.is_pressed('down'):
            finch.set_wheels(-50, -50) # backward

        elif keyboard.is_pressed('left'):
            finch.set_wheels(-30, 30) # turn left

        elif keyboard.is_pressed('right'):
            finch.set_wheels(30, -30) # turn right

        else:
            finch.set_wheels(0, 0) # stop

    time.sleep(0.05)

except KeyboardInterrupt:
    finch.set_wheels(0, 0)