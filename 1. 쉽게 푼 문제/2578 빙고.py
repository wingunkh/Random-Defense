def erase(n):
    for r in range(5):
        for c in range(5):
            if a[r][c] == n:
                a[r][c] = 0

def row_check():
    bingo = 0
    
    for row in a:
        if len(set(row)) == 1:
            bingo += 1

    return bingo

def col_check():
    bingo = 0
    cols = [[a[r][c] for r in range(5)] for c in range(5)]

    for col in cols:
        if len(set(col)) == 1:
            bingo += 1

    return bingo

def diagonal_check():
    bingo = 0
    diagonal1 = [a[i][i] for i in range(5)]
    diagonal2 = [a[i][4 - i] for i in range(5)]

    if len(set(diagonal1)) == 1:
        bingo += 1

    if len(set(diagonal2)) == 1:
        bingo += 1

    return bingo

a = [list(map(int, input().split())) for _ in range(5)]
b = [list(map(int, input().split())) for _ in range(5)]
result = 0

for r in range(5):
    for c in range(5):
        result += 1
        bingo = 0
        
        erase(b[r][c])
        bingo += row_check()
        bingo += col_check()
        bingo += diagonal_check()

        if bingo >= 3:
            print(result)
            exit()
