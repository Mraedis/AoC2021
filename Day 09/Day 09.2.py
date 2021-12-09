from collections import Counter
terrain = [[int(c) for c in line.strip()] for line in open('Day 09.input')]

for t in terrain:
    t.insert(0, 9)
    t.append(9)
terrain.insert(0, [9] * len(terrain[0]))
terrain.append([9] * len(terrain[0]))

total = 0
lows = []
neighbours = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def basin(bx, by):
    low = False
    for bdx, bdy in neighbours:
        if terrain[bx][by] > terrain[bx + bdx][by + bdy]:
            low = (bx + bdx, by + bdy)
    if not low:
        return bx, by
    else:
        return basin(low[0], low[1])


basins = []
for x in range(1, len(terrain)-1):
    for y in range(1, len(terrain[0])-1):
        tile = terrain[x][y]
        if tile != 9:
            basins.append(basin(x, y))

size = 1
for b in sorted([basins.count(x) for x in set(basins)])[-3:]:
    size *= b
print(size)
