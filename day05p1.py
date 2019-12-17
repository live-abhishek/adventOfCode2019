import sys
sys.stdin = open("day3.txt")

inp = [int(i) for i in input().split(",")]

class IntCodeComputer:
    def __init__(self, code):
        self.inp = code
        self.userInput = 1
        self.__currPos = 0

    def process(self):
        while self.__currPos < len(self.inp):
            opcode = self.__nextCode()
            opcode = self.__opcodeWithMode(opcode)
            modes, code = opcode[:3], opcode[3:]
            modes = modes[::-1]
            self.__incPtr()
            if code == "01":
                self.__add(modes)
            if code == "02":
                self.__mul(modes)
            if code == "03":
                self.__saveInput()
            if code == "04":
                self.__output(modes)
            if code == "99":
                self.__incPtr()
                break

    def __add(self, modes):
        num1 = self.__num(modes[0])
        self.__incPtr()
        num2 = self.__num(modes[1])
        self.__incPtr()
        resPos = self.__nextCode()
        self.__incPtr()
        res = num1 + num2
        self.inp[resPos] = res

    def __mul(self, modes):
        num1 = self.__num(modes[0])
        self.__incPtr()
        num2 = self.__num(modes[1])
        self.__incPtr()
        resPos = self.__nextCode()
        self.__incPtr()
        res = num1 * num2
        self.inp[resPos] = res

    def __num(self, mode):
        return self.inp[self.__nextCode()] if mode == "0" else self.__nextCode()


    def __saveInput(self):
        pos = self.__nextCode()
        self.__incPtr()
        self.inp[pos] = self.userInput

    def __output(self, modes):
        ans = self.__num(modes[0])
        print(ans)
        self.__incPtr()

    def __incPtr(self):
        self.__currPos += 1

    def __nextCode(self):
        return self.inp[self.__currPos]

    def __opcodeWithMode(self, opcode):
        return f"{opcode:05}"

computer = IntCodeComputer(inp)
computer.process()

