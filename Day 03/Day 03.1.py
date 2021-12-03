linelist = [line for line in open('Day 03.input').readlines()]

g_rate = 0
e_rate = 0
length = 0
counter = [0] * (len(linelist[0]) - 1)

for line in linelist:
    for i in range(0, len(line) - 1):
        counter[i] += int(line[i])
    length += 1

for i in range(0, len(counter)):
    if counter[i] > (length / 2):
        g_rate += 2 ** (len(counter) - i - 1)
    else:
        e_rate += 2 ** (len(counter) - i - 1)

print(g_rate * e_rate)
