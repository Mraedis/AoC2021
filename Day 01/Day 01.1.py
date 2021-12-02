linelist = [int(val) for val in open('Day 01.input').readlines()]
increases = 0
previous = linelist[0]

for line in linelist[1:]:
    if previous < line:
        increases += 1
    previous = line
print(increases)
