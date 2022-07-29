import serial
import time

port = "COM3"
ser = serial.Serial(port, 9600)
while True:
    if ser.inWaiting() > 0:
        print(ser.readline().decode("utf-8".strip()))