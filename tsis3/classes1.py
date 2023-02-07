class InputOutString(object):
    def __init__(self):
        self.s = " "

    def getString(self):
        self.s = input()

    def printString(self):
        print (self.s.upper())

str = InputOutString()
str.getString()
str.printString()