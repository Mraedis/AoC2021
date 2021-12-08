sevseg = {0: 'abcefg', 1: 'cf', 2: 'acdeg', 3: 'acdfg', 4: 'bcdf',
          5: 'abdfg', 6: 'abdefg', 7: 'acf', 8: 'abcdefg', 9: 'abcdfg'}
up = [line.strip().split(' | ')[1] for line in open('Day 08.input')]

total = 0
for u in up:
    total += sum(len(x) in [2, 3, 4, 7] for x in u.split(' '))
print(total)
