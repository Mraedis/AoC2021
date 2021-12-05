vals = {}
for line in open('Day 05.input'):
    x0, y0, x1, y1 = [int(c) for p in line.split(' -> ') for c in p.split(',')]
    if x0 == x1:
        for i in range(min(y0, y1), max(y0, y1)+1):
            vals[x0, i] = vals.get((x0, i), 0) + 1
    elif y0 == y1:
        for i in range(min(x0, x1), max(x0, x1)+1):
            vals[i, y0] = vals.get((i, y0), 0) + 1

print(sum(x > 1 for x in vals.values()))
