import serial
import time
import utils
import keyboard

port = utils.select_port()
ser = serial.Serial(port, 9600)
while True:
    if ser.inWaiting() > 0:
        print(ser.readline().decode("utf-8".strip()))