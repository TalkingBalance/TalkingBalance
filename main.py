import serial
import time
import utils
import keyboard

port = utils.select_port()
ser = serial.Serial(port, 9600)
keyboard.add_hotkey("t", utils.send_command, args=[ser, "T", "Now tared."])
while True:
    if ser.inWaiting() > 0:
        print(ser.readline().decode("utf-8".strip()))