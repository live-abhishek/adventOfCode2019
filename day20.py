lines = open("day20.txt").read().splitlines()

# convert list of lines to list of list of strings
graph = [list(line) for line in lines]
seenNodes = set()

def isChar(c):
    return ord('A') <= ord(c) <= ord('Z')

for r in range(len(graph)):
    for c in range(len(graph[0])):
        if lines[r][c] == ".":
            if isChar(lines[r-1][c]):
                nodeName = lines[r-2][c] + lines[r-1][c]
                nodeName = nodeName + "2" if nodeName + "1" in seenNodes else nodeName + "1"
                graph[r][c] = nodeName
                graph[r-2][c] = " "
                graph[r-1][c] = " "
                seenNodes.add(nodeName)
            elif isChar(lines[r+1][c]):
                nodeName = lines[r+1][c] + lines[r+2][c]
                nodeName = nodeName + "2" if nodeName + "1" in seenNodes else nodeName + "1"
                graph[r][c] = nodeName
                graph[r+1][c] = " "
                graph[r+2][c] = " "
                seenNodes.add(nodeName)
            elif isChar(lines[r][c-1]):
                nodeName = lines[r][c-2] + lines[r][c-1]
                nodeName = nodeName + "2" if nodeName + "1" in seenNodes else nodeName + "1"
                graph[r][c] = nodeName
                graph[r][c-1] = " "
                graph[r][c-2] = " "
                seenNodes.add(nodeName)
            elif isChar(lines[r][c+1]):
                nodeName = lines[r][c+1] + lines[r][c+2]
                nodeName = nodeName + "2" if nodeName + "1" in seenNodes else nodeName + "1"
                graph[r][c] = nodeName
                graph[r][c+1] = " "
                graph[r][c+2] = " "
                seenNodes.add(nodeName)
graph.pop(0)
graph.pop(0)
graph.pop()
graph.pop()
for line in graph:
    line.pop(0)
    line.pop(0)
    line.pop()
    line.pop()

edges = {}
seenNodes = set()

def traverse(r, c, startNode, cost):
    if r < 0 or r >= len(graph) or c < 0 or c >= len(graph[0]):
        return
    if graph[r][c] == ".":
        graph[r][c] = "@"
        traverse(r-1, c, startNode, cost + 1)
        traverse(r+1, c, startNode, cost + 1)
        traverse(r, c+1, startNode, cost + 1)
        traverse(r, c-1, startNode, cost + 1)
    if len(graph[r][c]) == 3:
        endNode = graph[r][c]
        if edges.get(startNode) is None:
            edges[startNode] = []
        if edges.get(endNode) is None:
            edges[endNode] = []
        edges[startNode].append((endNode, cost + 1))
        edges[endNode].append((startNode, cost + 1))

for r in range(len(graph)):
    for c in range(len(graph[0])):
        node = graph[r][c]
        if len(node) != 3:
            continue
        if node in seenNodes:
            continue
        graph[r][c] = "@"
        traverse(r-1, c, node, 0)
        traverse(r+1, c, node, 0)
        traverse(r, c+1, node, 0)
        traverse(r, c-1, node, 0)

# print(*graph, sep="\n")

for key in edges.keys():
    if key in ["AA1", "ZZ1"]:
        continue
    if key[-1] == "1":
        edges[key].append((key[:2] + "2", 1))
    else:
        edges[key].append((key[:2] + "1", 1))


for key in edges.keys():
    print(key, edges[key])



