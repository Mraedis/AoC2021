lf = list(map(int, open('Day 06.input').readline().split(',')))

for _ in range(80):
    for f in range(len(lf)):
        lf[f] -= 1
        if lf[f] < 0:
            lf[f] = 6
            lf.append(8)
print(len(lf))
