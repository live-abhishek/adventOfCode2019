def check(num):
    double = False
    increasing = True
    for i in range(1, len(num)):
        num1, num2 = int(num[i-1]), int(num[i])
        if num2 == num1:
            double = True
        elif num2 < num1:
            return False
    return double


def solve():
    low, high = 367479, 893698
    count = 0
    for n in range(low, high + 1):
        if check(str(n)):
            count += 1
    print(count)

solve()
