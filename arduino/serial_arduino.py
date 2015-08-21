__author__ = 'alexandre'
import serial
connected = False;
ser = serial.Serial('COM4', 9600, timeout=0)

while not connected:
    serin = ser.read()
    connected = True
ser.readl
ser.write(b'1')
r = ser.read()
ser.close()




