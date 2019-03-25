import serial
import time

"""
class Arduino:
    ser = serial.Serial('COM3')

    def __init__(port='COM3', baudrate=9600, timeout=0):
        ser = serial.Serial(port, baudrate, timeout=timeout)

    def get_line():
        return ser.readLine().decode().strip('\r\n')
"""


print("Starting arduino listener");
arduino = serial.Serial('COM3', 9600)

while True:
    print("arduino readline: {}".format(arduino.readLine()))
    time.sleep(1)
