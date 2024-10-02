def backtracking(depth):
    if depth == len(zero):
        for row in a:
            print(''.join(map(str, row)))

        exit()

    r, c = zero[depth]

    for i in range(1, 10):
        if row_check(r, i) and col_check(c, i) and square_check(r, c, i):
            a[r][c] = i
            backtracking(depth + 1)
            a[r][c] = 0

def row_check(r, number):
    for i in range(9):
        if a[r][i] == number:
            return False

    return True

def col_check(c, number):
    for i in range(9):
        if a[i][c] == number:
            return False

    return True

def square_check(r, c, number):
    nr = r // 3 * 3
    nc = c // 3 * 3

    for i in range(nr, nr + 3):
        for j in range(nc, nc + 3):
            if a[i][j] == number:
                return False

    return True

a = [list(map(int, input())) for _ in range(9)]
zero = []

for r in range(9):
    for c in range(9):
        if a[r][c] == 0:
            zero.append((r, c))

backtracking(0)
