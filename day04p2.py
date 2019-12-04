def check(num):
    increasing = True
    for i in range(1, len(num)):
        num1, num2 = int(num[i-1]), int(num[i])
        if num2 < num1:
            return False
    # here means all the numbers are in sorted order
    last = -1
    for i in range(len(num) - 1):
        if num[i] != num[i+1]:
            if i - last == 2:
                return True
            last = i
    if len(num) - 1 - last == 2:
        return True
    return False

def solve():
    low, high = 367479, 893698
    count = 0
    for n in range(low, high + 1):
        if check(str(n)):
            print(n)
            count += 1
    print(count)

solve()
