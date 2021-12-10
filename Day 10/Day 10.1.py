lines = [[c for c in line.strip()] for line in open('Day 10.input')]

total = 0
worth = {')': 3, ']': 57, '}': 1197, '>': 25137}
pairs = {'<': '>', '[': ']', '{': '}', '(': ')'}

for l in lines:
    closers = []
    invalid = None
    for c in l:
        if c in pairs.keys():
            closers.append(c)
        elif pairs[closers[-1]] == c:
            closers.pop()
        else:
            invalid = c
            break
    if invalid != None:
        total += worth[invalid]

print(total)
