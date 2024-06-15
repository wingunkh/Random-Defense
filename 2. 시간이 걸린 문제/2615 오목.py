def right(r, c):
    for i in range(c + 1, c + 5):
        if not (i <= 18) or a[r][i] != a[r][c]:
            return False

    if c + 5 <= 18 and a[r][c + 5] == a[r][c]:
        return False

    if c - 1 >= 0 and a[r][c - 1] == a[r][c]:
        return False

    return True

def bottom(r, c):
    for i in range(r + 1, r + 5):
        if not (i <= 18) or a[i][c] != a[r][c]:
            return False

    if r + 5 <= 18 and a[r + 5][c] == a[r][c]:
        return False

    if r - 1 >= 0 and a[r - 1][c] == a[r][c]:
        return False

    return True

def bottom_left(r, c):
    for i in range(1, 5):
        if not (r + i <= 18) or not (0 <= c - i <= 18) or a[r + i][c - i] != a[r][c]:
            return False

    if r + 5 <= 18 and c - 5 >= 0 and a[r + 5][c - 5] == a[r][c]:
        return False

    if r - 1 >= 0 and c + 1 <= 18 and a[r - 1][c + 1] == a[r][c]:
        return False

    return True

def bottom_right(r, c):
    for i in range(1, 5):
        if not (r + i <= 18) or not (c + i <= 18) or a[r + i][c + i] != a[r][c]:
            return False

    if r + 5 <= 18 and c + 5 <= 18 and a[r + 5][c + 5] == a[r][c]:
        return False

    if r - 1 >= 0 and c - 1 >= 0 and a[r - 1][c - 1] == a[r][c]:
        return False

    return True   

a = [list(map(int, input().split())) for _ in range(19)]

for r in range(19):
    for c in range(19):
        if a[r][c] != 0:
            if right(r, c) or bottom(r, c) or bottom_right(r, c):
                print(a[r][c])
                print(r + 1, c + 1)
                exit()
            elif bottom_left(r, c):
                print(a[r][c])
                print(r + 4 + 1, c - 4 + 1)
                exit()
else:
    print(0)
