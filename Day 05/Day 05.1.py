linelist = [[line.strip().split(' -> ')[0].split(','), line.strip().split(' -> ')[1].split(',')] for line in open('Day 05.input')]
pairs = []
for i in range(0, len(linelist)):
    x0 = linelist[i][0][1]
    y0 = linelist[i][0][0]
    x1 = linelist[i][1][1]
    y1 = linelist[i][1][0]
    pairs.append([[int(x0), int(y0)], [int(x1), int(y1)]])

vals = {}
for (x0, y0), (x1, y1) in pairs:
    if x0 == x1:
        for i in range(min(y0, y1), max(y0, y1)+1):
            vals[x0, i] = vals.get((x0, i), 0) + 1
    elif y0 == y1:
        for i in range(min(x0, x1), max(x0, x1)+1):
            vals[i, y0] = vals.get((i, y0), 0) + 1

intersects = sum(x > 1 for x in vals.values())
print(intersects)
