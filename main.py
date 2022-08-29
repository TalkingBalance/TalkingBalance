import time

import keyboard
import serial

import utils

print("Welcome to Talking Scientific Scales!")

try:
    port = utils.select_port()
except Exception as e:
    import sys
    input("Talking Scientific Scales could not find any compatible ports on your computer. If your scales aren't connected, please connect them and run the program again. If they are, please consult your IT department. Press enter to exit.")
    sys.exit()

ser = serial.Serial(port, 9600)

keyboard.add_hotkey("t", utils.send_command, args=[ser, "T", "Now tared."])
keyboard.add_hotkey("u", utils.send_command, args=[ser, "U", "Switched units."])
keyboard.add_hotkey("o", utils.send_command, args=[ser, "O", "Scales have been switched off."])
keyboard.add_hotkey("m", utils.send_command, args=[ser, "M", ""])
keyboard.add_hotkey("f", utils.send_command, args=[ser, "F", "Changing mode."])
keyboard.add_hotkey("c", utils.send_command, args=[ser, "C", "Calibration started."])
keyboard.add_hotkey("p", utils.send_command, args=[ser, "P", ""])


print(f"Using {port}. If you haven't already please turn your scales on.")

while True:
    if ser.inWaiting() > 0:
        print(ser.readline().decode("utf-8".strip()))
    time.sleep(0.01)