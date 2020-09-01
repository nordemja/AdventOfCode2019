fileName = open("C:\\Users\\justi\\Documents\\Python Programming\\AdventOfCode2019\\Day3Input.txt", 'r')

wires = [each.strip() for each in fileName.readlines()]
wires = [each.split(',') for each in wires]

def manhattanDistance(lst):
    return abs(lst[0]) + abs(lst[1])


distancesList = []
for path in wires:
    x, y = 0, 0
    steps = 0
    manhattanDict = dict()
    for p in path:
        direction, distance = p[0], int(p[1:])
        if direction == 'U':
            for i in range(1, distance+1):
                steps += 1
                if (x, y+i) not in manhattanDict:
                    manhattanDict[(x,y+i)] = steps
            x, y = x, y + distance
        elif direction == 'D':
            for i in range(1, distance+1):
                steps += 1
                if (x, y-i) not in manhattanDict:
                    manhattanDict[(x,y-i)] = steps
            x, y = x, y - distance
        elif direction == 'L':
            for i in range(1, distance+1):
                steps += 1
                if (x-i, y) not in manhattanDict:
                    manhattanDict[(x-i, y)] = steps
            x, y = x - distance, y
        elif direction == 'R':
            for i in range(1,distance+1):
                steps += 1
                if (x+i, y) not in manhattanDict:
                    manhattanDict[(x+i, y)] = steps
            x, y = x + distance, y

    distancesList.append(manhattanDict)

coordiantes = distancesList[0].keys() & distancesList[1].keys()
manhattanDistanceAnswer = min(coordiantes, key=manhattanDistance)
print("manhattan distance = " + str(manhattanDistance(manhattanDistanceAnswer)))

part2Answer = min(coordiantes, key = lambda x: distancesList[0][x] + distancesList[1][x])
print(distancesList[0][part2Answer] + distancesList[1][part2Answer])

fileName.close()