__author__ = 'alexandre'
import RPi.GPIO as io
import time
io.setmode(io.BCM)

io.setup(15, io.OUT)

def whatever():
        io.output(15, io.HIGH)
        time.sleep(3)
        io.output(15, io.LOW)
        time.sleep(1)



try:
    while True:
        whatever()
except KeyboardInterrupt:
    io.cleanup()

