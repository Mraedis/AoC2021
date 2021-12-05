linelist = [[line.strip().split(' -> ')[0].split(','), line.strip().split(' -> ')[1].split(',')] for line in open('Day 05.input').readlines()]
pairs = []
for i in range(0, len(linelist)):
    x0 = linelist[i][0][1]
    y0 = linelist[i][0][0]
    x1 = linelist[i][1][1]
    y1 = linelist[i][1][0]
    pairs.append([[int(x0), int(y0)], [int(x1), int(y1)]])

vals = {}
for (x0, y0), (x1, y1) in pairs:
    dx = 0 if x1 == x0 else (x1-x0)//abs(x1-x0)
    dy = 0 if y1 == y0 else (y1-y0)//abs(y1-y0)

    while x1 != x0 or y1 != y0:
        vals[x0, y0] = vals.get((x0, y0), 0) + 1
        x0 += dx
        y0 += dy
    vals[x0, y0] = vals.get((x0, y0), 0) + 1

intersects = sum(x > 1 for x in vals.values())
print(intersects)
