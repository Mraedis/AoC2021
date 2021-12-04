linelist = [line for line in open('Day 04.input').readlines()]

draws = linelist[0].strip().split(',')
b_side = 5

boards = []

for i in range(0, (int(len(linelist[1:]) / (b_side + 1)))):
    board = {}
    b_solved = [0] * (b_side * 2)
    for row in range(0, b_side):
        line = linelist[1 * (i + 1) + b_side * i + row + 1].strip()
        nums = line.strip().split()
        for col in range(0, b_side):
            board[nums[col]] = (row, col)
    boards.append([board, b_solved])

winner = False
c = 0
while not winner:
    draw = draws[c]
    for b in boards:
        if draw in b[0]:
            row, col = b[0][draw][0], b[0][draw][1]
            b[1][row] += 1
            b[1][b_side + col] += 1
        b[0].pop(draw, None)
        if 5 in b[1]:
            print(b[1])
            s = 0
            for k in b[0].keys():
                s += int(k)
            print(s * int(draw))
            winner = True
            break

    c += 1
