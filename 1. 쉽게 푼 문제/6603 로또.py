import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, depth):
    if depth == 6:
        print(' '.join(map(str, result)))
        return

    for i in range(x, n):
        result.append(a[i])
        dfs(i + 1, depth + 1)
        result.pop()

while True:
    buff = list(map(int, input().split()))
    n = buff[0]
    a = buff[1:]
    result = []
    
    if n == 0:
        break

    dfs(0, 0)
    print()
