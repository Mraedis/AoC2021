sevseg = {'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf': 4,
          'abdfg': 5, 'abdefg': 6, 'acf': 7, 'abcdefg': 8, 'abcdfg': 9}
sigdisp = [line.strip().split(' | ') for line in open('Day 08.input')]
total = 0

for signal, display in sigdisp:
    wires = sorted(signal.split(' '), key=len)
    digits = display.split(' ')

    # a,b,--- ,g
    mapper = {'a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f': '', 'g': ''}
    for c in wires[1]:
        if c not in wires[0]:
            mapper['a'] = c

    for c in 'abcdefg':
        occur = sum(c in w for w in wires)
        if occur == 4:
            mapper['e'] = c
        elif occur == 6:
            mapper['b'] = c
        elif occur == 8 and c != mapper['a']:
            mapper['c'] = c
        elif occur == 9:
            mapper['f'] = c
    for c in wires[2]:
        if c not in mapper['b'] + mapper['c'] + mapper['f']:
            mapper['d'] = c
    for c in 'abcdefg':
        if c not in mapper.values():
            mapper['g'] = c
    mapper = dict((v, k) for k, v in mapper.items())

    num = ''
    for d in digits:
        new_digit = ''
        for c in d:
            new_digit += mapper[c]
        num += str(sevseg[''.join(sorted(new_digit))])
    total += int(num)
print(total)
