import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
result = sys.maxsize

for r in range(n - 7):
    for c in range(m - 7):
        case_white = 0
        case_black = 0
        for i in range(r, r + 8):
            for j in range(c, c + 8):
                if (i + j) % 2 == 0:
                    if a[i][j] == 'W':
                        case_black += 1
                    else:
                        case_white += 1
                else:
                    if a[i][j] == 'W':
                        case_white += 1
                    else:
                        case_black += 1

        result = min(result, min(case_white, case_black))
                    
print(result)
