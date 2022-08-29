import re

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

    def readMessage(self):
        message = self.readRaw()
        parsedMessage = self.parseMessage(message)
        if parsedMessage['type'] == 'measurementMessage':
            return f"{parsedMessage['direction']} {parsedMessage['value']} {parsedMessage['units']}"
        else:
            return parsedMessage['raw']

    def parseMessage(self, message):
        parsed = {}
        parsed['raw'] = message
        parsed['direction'] = message[0] #+ or -
        parsed['value'] = re.search(r'\d.\d+|\d+', message).group() #0.002 or 0123 (LB doesn't include a point)
        parsed['units'] = re.search(r'[a-z]+', message).group() #g, lb, ct etc
        if None in parsed.values(): #If any of our expressions didn't return a match assume it's not a measurement message
            parsed['type'] = 'other'
        else:
            parsed['type'] = 'measurementMessage'
        return parsed

