__author__ = 'alexandre'
import time
import serial
import RPi.GPIO as gpio
ledPins = [2, 3, 4, 17]

ser = serial.Serial ('/dev/ttyUSB0', 9600)
ser.write('t')

resposta = ser.readline()
print 'distancia: %s' % resposta


def changeLed (idx):
    gpio.output(ledPins[idx], True)




