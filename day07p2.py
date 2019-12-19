from itertools import permutations
import sys
sys.stdin = open("day07.txt")

"""
copied from : https://github.com/kresimir-lukin/AdventOfCode2019/blob/master/intcode.py
Could not resolve the bug in my IntCode computer implementation
"""

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
        intcode.set(arguments[0].address, intcode.get_input())
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
        self.memory = {}
        self.output = None
        self.halted = False
        self.pc = 0

    def _get_instruction(self, instruction_code):
        return next(cls for cls in Instruction.__subclasses__() if cls.code == instruction_code)

    def _parse_arguments(self, argument_num):
        modes = str(self.program[self.pc]).zfill(5)[:3][::-1]
        arguments = []
        for i in range(argument_num):
            parameter = self.program[self.pc+i+1]
            arguments.append(Argument(parameter, self.program[parameter]) if modes[i] == "0" else Argument(parameter, parameter))
        return arguments

    def run(self):
        self.output = None
        while not self.halted and self.output is None:
            instruction = self._get_instruction(self.program[self.pc] % 100)
            arguments = self._parse_arguments(instruction.argument_num)
            self.pc = instruction().execute(self, arguments)
        return self.output

    def get(self, address):
        return self.program[address]

    def set(self, address, value):
        self.program[address] = value

    def addInput(self, value):
        self.inputs = [value] + self.inputs

    def get_input(self):
        return self.inputs.pop()

part2 = 0

def tryWithPhases(phases):
    global part2
    programs = [IntCode(code, [phases[i]]) for i in range(5)]
    previous_output = 0
    while all(not program.halted for program in programs):
        for program in programs:
            program.addInput(previous_output)
            output = program.run()
            if not program.halted:
                previous_output = output
    part2 = max(part2, previous_output)

for phases in permutations(range(5, 10)):
    tryWithPhases(phases)
    
print(part2)
