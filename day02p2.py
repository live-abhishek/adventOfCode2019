def check(noun, verb):
    inp = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,2,9,23,27,1,6,27,31,1,31,9,35,2,35,10,39,1,5,39,43,2,43,9,47,1,5,47,51,1,51,5,55,1,55,9,59,2,59,13,63,1,63,9,67,1,9,67,71,2,71,10,75,1,75,6,79,2,10,79,83,1,5,83,87,2,87,10,91,1,91,5,95,1,6,95,99,2,99,13,103,1,103,6,107,1,107,5,111,2,6,111,115,1,115,13,119,1,119,2,123,1,5,123,0,99,2,0,14,0]

    inp[1] = noun
    inp[2] = verb

    i = 0
    try:
        while True:
            opcode = inp[i]
            operand1Pos = inp[i + 1]
            operand2Pos = inp[i + 2]
            operand3Pos = inp[i + 3]
            if opcode == 1:
                inp[operand3Pos] = inp[operand1Pos] + inp[operand2Pos]
            elif opcode == 2:
                inp[operand3Pos] = inp[operand1Pos] * inp[operand2Pos]
            elif opcode == 99:
                return True if inp[0] == 19690720 else False
            else:
                return False
            i += 4
    except:
        return False
    

def solve():
    for i in range(100):
        for j in range(100):
            result = check(i, j)
            if result:
                print(i, j)
                return

solve()
print("done")
