import serial.tools.list_ports

def select_port():
    ports = serial.tools.list_ports.comports(include_links=False)
    if len(ports) == 1: return ports[0].name #No point in asking the user to choose a port if they only have one available
    print("Please select the port your scales are connected too from the following list:")
    print("If your scales do not appear in the below list, disconnect and reconnect them and then restart this program.")
    for i, port in enumerate(ports):
        print(f"{i+1}. {port.name}")
    print(f"Enter the number of the port you would like to connect too by entering a number between 1 and {i+1}")
    while True:
        chosenPort = input()
        if is_valid_port_number(ports, chosenPort): return ports[int(chosenPort)-1].name
        print(f"{chosenPort} is not a valid port number. Please try again.")

def is_valid_port_number(ports, chosenPort):
    if not chosenPort.isnumeric(): return False
    if 1 <= int(chosenPort) <= len(ports): return True
    return False

def send_command(ser, command, message):
    ser.write(str.encode(command))
    print(message)