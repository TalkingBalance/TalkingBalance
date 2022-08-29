from locale import currency
import re


class Scales:
    def __init__(self, ser):
        self.ser = ser
        # A dictionary of measurement units supported by the scales mapped to friendly names which are surfaced in measurement readings
        self.units = {
            "g": "grams",
            "oz": "ounces",
            "ozt": "troy ounces",
            "dwt": "pennyweights",
            "lb": "pounds",
            "ct": "carats"
        }
        self.currentUnit = 'unknown'

    def hasMessageToDisplay(self):
        if self.ser.inWaiting() > 0:
            return True
        else:
            return False

    def readRaw(self):
        return self.ser.readline().decode("utf-8").rstrip()

    def send_command(self, command, message):
        print(f"{message} {self.currentUnit}")
        self.ser.write(str.encode(command))
        if command == 'U':
            self.handleUnits()
            print(self.currentUnit)

    def readMessage(self):
        message = self.readRaw()
        parsedMessage = self.parseMessage(message)
        if parsedMessage['type'] == 'measurementMessage':
            self.currentUnit = parsedMessage['units']
            #return f"{parsedMessage['direction']} {parsedMessage['value']} {self.units[parsedMessage['units']]}"
            return parsedMessage['raw']
        else:
            return parsedMessage['raw']

    def parseMessage(self, message):
        parsed = {}
        parsed['raw'] = message
        parsed['direction'] = message[0]  # + or -
        # 0.002 or 0123 (LB doesn't include a point)
        parsed['value'] = re.search(r'\d.\d+|\d+', message).group()
        parsed['units'] = re.search(
            r'[a-z]+', message).group()  # g, lb, ct etc
        if None in parsed.values():  # If any of our expressions didn't return a match assume it's not a measurement message
            parsed['type'] = 'other'
        else:
            parsed['type'] = 'measurementMessage'
        return parsed

    def handleUnits(self):
        if self.currentUnit != 'unknown':
            for i, k in enumerate(self.units.keys()):
                if k == self.currentUnit:
                    print(f"k is {k} which is {self.currentUnit}")
                    if i == len(self.units)-1:
                        self.currentUnit = list(self.units.keys())[0]
                        break
                    else:
                        self.currentUnit = list(self.units.keys())[i+1]
                        break
