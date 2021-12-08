up = [line.strip().split(' | ')[1] for line in open('Day 08.input')]
print(sum(len(x) in [2, 3, 4, 7] for u in up for x in u.split(' ')))
