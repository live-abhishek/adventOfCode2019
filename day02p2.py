import sys
sys.stdin = open("day2.txt")

inp = [int(i) for i in input().split(",")]

class IntCodeComputer:
    def __init__(self, code):
        self.inp = code
        self.__currPos = 0

    def process(self):
        while self.__currPos < len(self.inp):
            opcode = self.__nextCode()
            self.__incPtr()
            if opcode == 1:
                self.__add()
            if opcode == 2:
                self.__mul()
            if opcode == 99:
                self.__incPtr()
                break

    def __add(self):
        num1 = self.inp[self.__nextCode()]
        self.__incPtr()
        num2 = self.inp[self.__nextCode()]
        self.__incPtr()
        resPos = self.__nextCode()
        self.__incPtr()
        self.inp[resPos] = num1 + num2

    def __mul(self):
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

for noun in range(100):
    for verb in range(100):
        newInp = inp[:]
        newInp[1] = noun
        newInp[2] = verb
        computer = IntCodeComputer(newInp)
        computer.process()
        if computer.inp[0] == 19690720:
            print(100*noun + verb)
            break

