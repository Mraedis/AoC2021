terrain = [[int(c) for c in line.strip()] for line in open('Day 09.input')]

for t in terrain:
    t.insert(0, 9)
    t.append(9)
terrain.insert(0, [9] * len(terrain[0]))
terrain.append([9] * len(terrain[0]))

total = 0
for x in range(1, len(terrain)-1):
    for y in range(1, len(terrain[0])-1):
        tile = terrain[x][y]
        neighbours = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        low = True
        for dx, dy in neighbours:
            if terrain[x+dx][y+dy] <= tile:
                low = False
        if low:
            total += terrain[x][y] + 1

print(total)
