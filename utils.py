import serial.tools.list_ports

def select_port():
    ports = serial.tools.list_ports.comports(include_links=False)
    print("Welcome to Talking Scientific Scales!")
    print("Please select the port your scales are connected to from the following list. You are looking for something like USB-to-serial adaptor.")
    print("If your scales do not appear in the below list, disconnect and reconnect them and then restart this program.")
    for i, port in enumerate(ports):
        print(i+1, ". ", port)
    print("Enter the number of the port you would like to connect to by entering a number between 1 and ", i+1, ", followed by the enter key.")
    # A sort of hack to get the port value as a string
    port = str(ports[int(input())-1]).split("(")[1].split(")")[0]
    return port

def send_command(ser, command, message):
    ser.write(str.encode(command))
    print(message)