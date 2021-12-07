horpos = list(map(int, open('Day 07.input').readline().split(',')))
mean = sum(horpos) / len(horpos)
target1 = mean - (mean % 1)
target2 = mean + (1 - mean % 1)
print(min(round(sum((abs(x - target1) * (abs(x - target1) + 1)) / 2 for x in horpos)),
          round(sum((abs(x - target2) * (abs(x - target2) + 1)) / 2 for x in horpos))))
