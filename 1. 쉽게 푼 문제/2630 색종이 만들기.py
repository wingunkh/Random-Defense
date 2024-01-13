def func(row, col, length):
    global white, blue
    for r in range(row, row + length):
        for c in range(col, col + length):
            if a[r][c] != a[row][col]:
                func(row, col, length // 2)
                func(row, col + length // 2, length // 2)
                func(row + length // 2, col, length // 2)
                func(row + length // 2, col + length // 2, length // 2)
                
                return

    if a[row][col] == 0:
        white += 1
    else:
        blue += 1

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
white = 0
blue = 0

func(0, 0, n)

print(white)
print(blue)
