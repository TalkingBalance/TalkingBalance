import serial
import time
import serial.tools.list_ports
ports = serial.tools.list_ports.comports(include_links=False)
for i, port in enumerate(ports):
    print(i+1, ". ", port)
print("Enter the number of the port you would like to connect to by entering a number between 1 and ", i+1)
# A sort of hack to get the port value as a string
port = str(ports[int(input())-1]).split("(")[1].split(")")[0]
print("Got the port ", port)
ser = serial.Serial(port, 9600)
while True:
    if ser.inWaiting() > 0:
        print(ser.readline().decode("utf-8".strip()))