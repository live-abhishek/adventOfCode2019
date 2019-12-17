import sys
sys.stdin = open("day2.txt")

inp = [int(i) for i in input().split(",")]
inp[1] = 12
inp[2] = 2

class IntCodeComputer:
    def __init__(self, code):
        self.inp = code
        self.__currPos = 0

    def process(self):
        while self.__currPos < len(self.inp):
            opcode = self.__nextCode()
            if opcode == 1:
                self.__add()
            if opcode == 2:
                self.__mul()
            if opcode == 99:
                self.__incPtr()
                break

    def __add(self):
        self.__incPtr()
        num1 = self.inp[self.__nextCode()]
        self.__incPtr()
        num2 = self.inp[self.__nextCode()]
        self.__incPtr()
        resPos = self.__nextCode()
        self.__incPtr()
        self.inp[resPos] = num1 + num2

    def __mul(self):
        self.__incPtr()
        num1 = self.inp[self.__nextCode()]
        self.__incPtr()
        num2 = self.inp[self.__nextCode()]
        self.__incPtr()
        resPos = self.__nextCode()
        self.__incPtr()
        self.inp[resPos] = num1 * num2

    def __incPtr(self):
        self.__currPos += 1

    def __nextCode(self):
        return self.inp[self.__currPos]

computer = IntCodeComputer(inp)
computer.process()
print(computer.inp[0])
