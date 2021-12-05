linelist = [[line.strip().split(' -> ')[0].split(','), line.strip().split(' -> ')[1].split(',')] for line in open('Day 05.input').readlines()]
pairs = []
for i in range(0, len(linelist)):
    x0 = linelist[i][0][0]
    y0 = linelist[i][0][1]
    x1 = linelist[i][1][0]
    y1 = linelist[i][1][1]
    pairs.append([[int(x0), int(y0)], [int(x1), int(y1)]])

grid = [[0 for col in range(1000)] for row in range(1000)]
for pair in pairs:
    y0 = pair[0][0]
    x0 = pair[0][1]
    y1 = pair[1][0]
    x1 = pair[1][1]
    if x0 == x1:
        for i in range(min(y0, y1), max(y0, y1)+1):
            grid[x0][i] += 1
    elif y0 == y1:
        for i in range(min(x0, x1), max(x0, x1)+1):
            grid[i][y1] += 1

intersects = 0
for line in grid:
    intersects += sum(x > 1 for x in line)
print(intersects)
