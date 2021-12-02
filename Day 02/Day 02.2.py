linelist = [line for line in open('Day 02.input').readlines()]

hor = 0
dep = 0
aim = 0

for line in linelist:
    mov, amount = line.split(' ')
    amount = int(amount)
    if mov == 'forward':
        hor += amount
        dep += aim * amount
    else:
        aim += amount * (-1 if mov == 'up' else 1)
print(hor * dep)
