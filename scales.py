class Scales:
    def __init__(self, ser):
        self.ser = ser

    def hasMessageToDisplay(self):
        if self.ser.inWaiting() > 0:
            return True
        else:
            return False

    def readRaw(self):
        return self.ser.readline().decode("utf-8").rstrip()
    
    def send_command(self, command, message):
        self.ser.write(str.encode(command))
        print(message)
