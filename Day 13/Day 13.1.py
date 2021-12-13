dots = {tuple([int(c) for c in l.strip().split(',')]): True for l in open('Day 13.1.input')}
folds = [(l.split('=')[0][-1], int(l.split('=')[1].strip())) for l in open('Day 13.2.input')]

for xy, vec in folds:
    newd = {}
    if xy == 'y':
        for x, y in dots.keys():
            if y < vec:
                newd[(x, y)] = True
            else:
                newd[(x, vec - (y - vec))] = True
    else:
        for x, y in dots.keys():
            if x < vec:
                newd[(x, y)] = True
            else:
                newd[(vec - (x - vec), y)] = True
    dots = newd
    break

print(sum(dots.values()))
