def dfs(x, depth):
    if depth == m:
        print(' '.join(map(str, result)))

        return

    for i in range(x, n + 1):
        result.append(i)
        dfs(i, depth + 1)
        result.pop()
        
n, m = map(int, input().split())
a = [i for i in range(1, n + 1)]
result = []

dfs(1, 0)
