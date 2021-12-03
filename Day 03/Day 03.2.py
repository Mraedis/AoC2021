linelist = [line.strip() for line in open('Day 03.input').readlines()]

oxy_rating = 0
lsp_rating = 0
length = len(linelist[0])
bits = [0] * length
orl = linelist
lrl = linelist

counter = [0] * length
for i in range(0, length):
    lines = 0
    for line in orl:
        counter[i] += int(line[i])
        lines += 1
    newlinelist = []
    if len(orl) <= 1:
        break
    for line in orl:
        if int(line[i]) == (int(counter[i] >= (lines / 2))):
            newlinelist.append(line)
    orl = newlinelist

counter = [0] * length
for i in range(0, length):
    lines = 0
    for line in lrl:
        counter[i] += int(line[i])
        lines += 1
    newlinelist = []
    if len(lrl) <= 1:
        break
    for line in lrl:
        if int(line[i]) != (int(counter[i] >= (lines / 2))):
            newlinelist.append(line)
    lrl = newlinelist

for i in range(0, len(lrl[0])):
    oxy_rating += int(orl[0][i]) * 2 ** (len(orl[0]) - i - 1)
    lsp_rating += int(lrl[0][i]) * 2 ** (len(lrl[0]) - i - 1)

print(oxy_rating * lsp_rating)

