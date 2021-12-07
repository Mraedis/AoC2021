horpos = list(map(int, open('Day 07.input').readline().split(',')))
horpos.sort()
median = horpos[len(horpos)//2]
print(sum(abs(x - median) for x in horpos))
