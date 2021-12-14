lines = [l.strip() for l in open('Day 14.input')]
target = lines[0]
repl = {l.split(' -> ')[0]: l.split(' -> ')[1] for l in lines[1:]}

for _ in range(10):
    ntarget = target[-1]
    l = len(target)
    for i in range(l):
        t = target[l-i-2:l-i]
        if t in repl.keys():
            ntarget = target[l-i-2] + repl[t] + ntarget
        else:
            ntarget = t + ntarget
    target = ntarget

occur = {}
letters = set(target)
for l in letters:
    occur[target.count(l)] = l
s = sorted(occur.keys())
print(s[-1] - s[0])
