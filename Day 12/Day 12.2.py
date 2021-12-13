edges = [tuple(l.strip().split('-')) for l in open('Day 12.input')]
nodes = {}

for s, e in edges:
    if s not in nodes:
        nodes[s] = set()
    nodes[s].add(e)
    if e not in nodes:
        nodes[e] = set()
    nodes[e].add(s)

for _ in nodes.values():
    _.discard('start')

paths = [[False, 'start', nxt] for nxt in nodes['start']]

while not all('end' in p for p in paths):
    newp = []
    for p in paths:
        last = p[-1]
        if last != 'end':
            for q in nodes[last]:
                if q.isupper():
                    newp.append(p + [q])
                elif q not in p:
                    newp.append(p + [q])
                elif not p[0]:
                    n = p.copy()
                    n[0] = True
                    newp.append(n + [q])
        else:
            newp.append(p)
    paths = newp
print(len(paths))
