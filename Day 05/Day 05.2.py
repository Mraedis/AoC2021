vals = {}
for line in open('Day 05.input'):
    x0, y0, x1, y1 = [int(c) for p in line.split(' -> ') for c in p.split(',')]
    dx = 0 if x1 == x0 else (x1-x0)//abs(x1-x0)
    dy = 0 if y1 == y0 else (y1-y0)//abs(y1-y0)

    while x1 != x0 or y1 != y0:
        vals[x0, y0] = vals.get((x0, y0), 0) + 1
        x0 += dx
        y0 += dy
    vals[x0, y0] = vals.get((x0, y0), 0) + 1

intersects = sum(x > 1 for x in vals.values())
print(intersects)
