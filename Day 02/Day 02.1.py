linelist = [line for line in open('Day 02.input').readlines()]

hor = 0
dep = 0

for line in linelist:
    mov, amount = line.split(' ')
    if mov == 'forward':
        hor += int(amount)
    else:
        dep += int(amount) * (-1 if mov == 'up' else 1)
print(hor * dep)
