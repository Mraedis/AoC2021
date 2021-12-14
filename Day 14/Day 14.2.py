lines = [l.strip() for l in open('Day 14.input')]
target = lines[0]
repl = {l.split(' -> ')[0] : l.split(' -> ')[1] for l in lines[1:]}

occur = {k: 0 for k in repl.keys()}
for i in range(len(target[:-1])):
    occur[target[i:i+2]] += 1

for _ in range(40):
    noccur = occur.copy()
    for k in noccur.keys():
        t = repl[k]
        occur[k[0] + t] += noccur[k]
        occur[t + k[1]] += noccur[k]
        occur[k] -= noccur[k]

counts = {target[-1]: 1}
for k, v in occur.items():
    counts[k[0]] = v if k[0] not in counts else counts[k[0]] + v
s = sorted(counts.values())
print(s[-1] - s[0])
