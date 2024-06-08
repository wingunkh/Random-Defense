def check():
    global result
    
    for c in range(n): # ↓ 방향
        length = 1
        
        for r in range(n - 1):
            if a[r][c] == a[r + 1][c]:
                length += 1
            else:
                result = max(result, length)
                length = 1

        result = max(result, length)


    for r in range(n): # → 방향
        length = 1

        for c in range(n - 1):
            if a[r][c] == a[r][c + 1]:
                length += 1
            else:
                result = max(result, length)
                length = 1

        result = max(result, length)

n = int(input())
a = [list(input()) for _ in range(n)]
change = []
result = 0

for c in range(n): # ↓ 방향
    for r in range(n - 1):
        if a[r][c] != a[r + 1][c]:
            change.append((r, c, r + 1, c))

for r in range(n): # → 방향
    for c in range(n - 1):
        if a[r][c] != a[r][c + 1]:
            change.append((r, c, r, c + 1))

for r1, c1, r2, c2 in change:
    a[r1][c1], a[r2][c2] = a[r2][c2], a[r1][c1]

    check()

    a[r1][c1], a[r2][c2] = a[r2][c2], a[r1][c1]

print(result)
