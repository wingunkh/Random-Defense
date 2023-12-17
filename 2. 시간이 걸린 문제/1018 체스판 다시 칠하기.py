import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(input().rstrip()) for _ in range(n)]
result = sys.maxsize

for r in range(n-7):
    for c in range(m-7):
        case_white_start = 0
        case_black_start = 0
        for i in range(r, r+8):
            for j in range(c, c+8):
                if (i+j) % 2 == 0:
                    if a[i][j] == 'W':
                        case_black_start += 1
                    else:
                        case_white_start += 1
                else:
                    if a[i][j] == 'W':
                        case_white_start += 1
                    else:
                        case_black_start += 1

        result = min(result, case_white_start, case_black_start)

print(result)
