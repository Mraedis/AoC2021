linelist = [int(val) for val in open('Day 01.input').readlines()]
increases = 0

p1 = linelist[0]
p2 = linelist[1]
p3 = linelist[2]
s1 = p1 + p2 + p3

for line in linelist[3:]:
    s2 = s1 + line - p1
    if s2 > s1:
        increases += 1
    p1 = p2
    p2 = p3
    p3 = line
print(increases)
