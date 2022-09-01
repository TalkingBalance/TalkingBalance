import serial.tools.list_ports

def select_port():
    ports = serial.tools.list_ports.comports(include_links=False)
    if len(ports) == 1: return ports[0].name #No point in asking the user to choose a port if they only have one available
    print("Please select the port your scales are connected too from the following list:")
    print("If your scales do not appear in the below list, disconnect and reconnect them and then restart this program.")
    for i, port in enumerate(ports):
        print(f"{i+1}. {port}")
    print(f"Enter the number of the port you would like to connect too by entering a number between 1 and {i+1} followed by the enter key.")
    while True:
        chosenPort = input()
        if is_valid_port_number(ports, chosenPort): return ports[int(chosenPort)-1].name
        print(f"{chosenPort} is not a valid port number. Please try again.")

def is_valid_port_number(ports, chosenPort):
    if not chosenPort.isnumeric(): return False
    if 1 <= int(chosenPort) <= len(ports): return True
    return False

def scales_turned_off_choice():
    print("The scales have now been turned off. Would you like to exit? [y/n]")
    exit = input()
    if exit == "y" or exit == "yes":
        print("Exiting...")
        import sys
        sys.exit()
    else:
        print("The program will stay open until closed with Control+C")
