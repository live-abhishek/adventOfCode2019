import sys
sys.stdin = open("day09.txt")

code = [int(i) for i in input().split(",")]

class Instruction:
    code, argument_num = 0, 0
    def execute(self, intcode, arguments):
        pass
    def new_pc(self, intcode):
        return intcode.pc + self.argument_num + 1

class PlusInstruction(Instruction):
    code, argument_num = 1, 3
    def execute(self, intcode, arguments):
        intcode.set(arguments[2].address, arguments[0].value + arguments[1].value)
        return self.new_pc(intcode)

class MultiplyInstruction(Instruction):
    code, argument_num = 2, 3
    def execute(self, intcode, arguments):
        intcode.set(arguments[2].address, arguments[0].value * arguments[1].value)
        return self.new_pc(intcode)

class InputInstruction(Instruction):
    code, argument_num = 3, 1
    def execute(self, intcode, arguments):
        intcode.set(arguments[0].address, intcode.getInput())
        return self.new_pc(intcode)

class OutputInstruction(Instruction):
    code, argument_num = 4, 1
    def execute(self, intcode, arguments):
        intcode.output = arguments[0].value
        return self.new_pc(intcode)

class JumpIfTrueInstruction(Instruction):
    code, argument_num = 5, 2
    def execute(self, intcode, arguments):
        return arguments[1].value if arguments[0].value != 0 else self.new_pc(intcode)

class JumpIfFalseInstruction(Instruction):
    code, argument_num = 6, 2
    def execute(self, intcode, arguments):
        return arguments[1].value if arguments[0].value == 0 else self.new_pc(intcode)

class LessThanInstruction(Instruction):
    code, argument_num = 7, 3
    def execute(self, intcode, arguments):
        intcode.set(arguments[2].address, int(arguments[0].value < arguments[1].value))
        return self.new_pc(intcode)

class EqualsInstruction(Instruction):
    code, argument_num = 8, 3
    def execute(self, intcode, arguments):
        intcode.set(arguments[2].address, int(arguments[0].value == arguments[1].value))
        return self.new_pc(intcode)

class RelativeBaseInstruction(Instruction):
    code, argument_num = 9, 1
    def execute(self, intcode, arguments):
        intcode.relativeBase += arguments[0].value
        return self.new_pc(intcode)

class HaltInstruction(Instruction):
    code, argument_num = 99, 0
    def execute(self, intcode, arguments):
        intcode.halted = True
        return None

class Argument:
    def __init__(self, address, value):
        self.address = address
        self.value = value
        
class IntCode:
    def __init__(self, program, inputs=[]):
        self.program = program[:]
        self.inputs = inputs[::-1]
        self.output = None
        self.halted = False
        self.pc = 0
        self.relativeBase = 0
        self.memory = {} # better to use dict instead of array because I don't know the max memory required

    def _get_instruction(self, instruction_code):
        return next(cls for cls in Instruction.__subclasses__() if cls.code == instruction_code)

    def _parse_arguments(self, argument_num):
        modes = str(self.program[self.pc]).zfill(5)[:3][::-1]
        arguments = []
        for i in range(argument_num):
            address = None
            value = None
            parameter = self.program[self.pc + i + 1]

            if modes[i] == "0":
                address = parameter
                value = self.getValue(address)
            elif modes[i] == "1":
                address = parameter
                value = address
            elif modes[i] == "2":
                address = parameter + self.relativeBase
                value = self.getValue(address)

            arguments.append(Argument(address, value))
        return arguments

    def run(self):
        self.output = None
        while not self.halted and self.output is None:
            instruction = self._get_instruction(self.program[self.pc] % 100)
            arguments = self._parse_arguments(instruction.argument_num)
            self.pc = instruction().execute(self, arguments)
        return self.output

    def getValue(self, address):
        return self.program[address] if address < len(self.program) else self.memory.get(address, 0)

    def set(self, address, value):
        programOrMemory = self.program if address < len(self.program) else self.memory
        programOrMemory[address] = value

    def addInput(self, value):
        self.inputs = [value] + self.inputs

    def getInput(self):
        return self.inputs.pop()

    def executeTillHalt(self):
        last_output = None
        while not self.halted:
            output = self.run()
            if not self.halted:
                last_output = output
        return last_output

program = IntCode(code, [1])
output = program.executeTillHalt()
print(output)
