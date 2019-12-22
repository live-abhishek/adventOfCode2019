import math

astroMap = open("day10.txt").read().splitlines()


def getAngle(start, end):
    result = (math.atan2(end[0] - start[0],
                         end[1] - start[1]) * 180 / math.pi)
    if result < 0:
        return 360 + result
    return result


def dist(start, end):
    return (start[0] - end[0])**2 + (start[1] - end[1])**2


def calcFromPoint(startX, startY):
    angles = {}
    for c in range(len(astroMap)):
        for r in range(len(astroMap[0])):
            if c == startX and r == startY:
                continue
            # compute all angles
            if astroMap[c][r] == "#":
                angle = getAngle((startX, startY), (c, r))
                if angles.get(angle) is None:
                    angles[angle] = []
                angles[angle].append((r, c))
    return angles


maxReachable = -1
cordinates = (-1, -1)


def solve1():
    global maxReachable
    global cordinates
    for x in range(len(astroMap)):
        for y in range(len(astroMap[0])):
            if astroMap[x][y] == "#":
                reachableAstro = calcFromPoint(x, y)
                if len(reachableAstro) > maxReachable:
                    maxReachable = len(reachableAstro)
                    cordinates = (x, y)
    print(maxReachable)
    print(cordinates)


solve1()


def solve2():
    angles = calcFromPoint(*cordinates)
    for angle in angles.keys():
        sortedPoints = sorted(angles[angle], key=lambda c: dist(cordinates, c))
        sortedPoints.reverse()
        angles[angle] = sortedPoints
    sortedAngles = sorted(angles.keys(), key=lambda a: (a + 90) % 360)
    for angle in sortedAngles:
        print(angle, angles[angle])
    cnt = 1
    lastAngleIdx = 0
    while cnt < 200:
        angle = sortedAngles[lastAngleIdx]
        lastAngleIdx += 1
        if len(angles[angle]) == 0:
            continue
        print(angles[angle][-1])
        angles[angle].pop()
        cnt += 1
    finalAngle = sortedAngles[lastAngleIdx]
    print(angles[finalAngle][-1])


solve2()
