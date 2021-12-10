lines = [[c for c in line.strip()] for line in open('Day 10.input')]

scores = []
worth = {')': 1, ']': 2, '}': 3, '>': 4}
pairs = {'<': '>', '[': ']', '{': '}', '(': ')'}
uncorrupted = []

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
    if invalid == None:
        uncorrupted.append(l)

for l in uncorrupted:
    closers = []
    invalid = None
    for c in l:
        if c in pairs.keys():
            closers.append(c)
        elif pairs[closers[-1]] == c:
            closers.pop()
    closers.reverse()
    temp = 0
    for c in closers:
        temp *= 5
        temp += worth[pairs[c]]
    scores.append(temp)
print(sorted(scores)[len(scores)//2])
