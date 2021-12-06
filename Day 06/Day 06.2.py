lf = list(map(int, open('Day 06.input').readline().split(',')))

fish = [lf.count(num) for num in range(9)]
for _ in range(256):
    num = fish.pop(0)
    fish[6] += num
    fish.append(num)
print(sum(fish))

