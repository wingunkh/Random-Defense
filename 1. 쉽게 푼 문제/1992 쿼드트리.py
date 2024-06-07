def func(r, c, length):
    if check(r, c, length):
        print(a[r][c], end = '')

        return

    length //= 2

    print('(', end= '')
    func(r, c, length)
    func(r, c + length, length)
    func(r + length, c, length)
    func(r + length, c + length, length)
    print(')', end = '')

def check(r, c, length):
    for i in range(r, r + length):
        for j in range(c, c + length):
            if a[i][j] != a[r][c]:
                return False

    return True

n = int(input())
a = [list(map(int, input())) for _ in range(n)]

func(0, 0, n)
