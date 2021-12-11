octopi = [[int(c) for c in line.strip()] for line in open('Day 11.input')]

s = 10
flashes = 0
flashed = [[False] * s for i in range(s)]


def flash(o, fx, fy):
    o[fx][fy] += 1
    if o[fx][fy] > 9 and not flashed[fx][fy]:
        flashed[fx][fy] = True
        for fi in range(max(fx - 1, 0), min(fx + 2, s)):
            for fj in range(max(fy - 1, 0), min(fy + 2, s)):
                flash(o, fi, fj)


for _ in range(100):
    for x in range(s):
        for y in range(s):
            flash(octopi, x, y)

    for x in range(s):
        for y in range(s):
            if octopi[x][y] > 9:
                octopi[x][y] = 0
                flashes += 1
            flashed[x][y] = False
print(flashes)
