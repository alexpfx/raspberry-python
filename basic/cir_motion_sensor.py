__author__ = 'alexandre'
import time
import RPi.GPIO as io
io.setmode(io.BOARD)
io.setup(7, io.IN)

def motion_detection():
    try:
        while True:
            time.sleep(2)
            if (io.input (7) == 1):
                print("Motion")
            else:
                print("No motion")
    except KeyboardInterrupt:
        io.cleanup()
        exit()

motion_detection()