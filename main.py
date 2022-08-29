import time

import keyboard
import serial

import scales
import utils

print("Welcome to Talking Scientific Scales!")

try:
    port = utils.select_port()
except Exception as e:
    import sys
    input("Talking Scientific Scales could not find any compatible ports on your computer. If your scales aren't connected, please connect them and run the program again. If they are, please consult your IT department. Press enter to exit.")
    sys.exit()

ser = serial.Serial(port, 9600)
scales = scales.Scales(ser)

keyboard.add_hotkey("t", scales.send_command, args=["T", "Now tared."])
keyboard.add_hotkey("u", scales.send_command, args=["U", "Switched units."])
keyboard.add_hotkey("o", scales.send_command, args=["O", "Scales have been switched off."])
keyboard.add_hotkey("m", scales.send_command, args=["M", ""])
keyboard.add_hotkey("f", scales.send_command, args=["F", "Changing mode."])
keyboard.add_hotkey("c", scales.send_command, args=["C", "Calibration started."])
keyboard.add_hotkey("p", scales.send_command, args=["P", ""])


print(f"Using {port}. If you haven't already please turn your scales on.")

while True:
    if scales.hasMessageToDisplay():
        print(scales.readRaw())
    time.sleep(0.01)