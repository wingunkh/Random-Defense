def dfs(r, c, depth):
    global result

    result = max(result, depth)
        
    for i in range(4):
        next_r, next_c = r + dr[i], c+ dc[i]

        if 0 <= next_r < n and 0 <= next_c < m and a[next_r][next_c] not in alphabet:
            alphabet.add(a[next_r][next_c])
            dfs(next_r, next_c, depth+1)
            alphabet.remove(a[next_r][next_c])

n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
alphabet = set()
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = 0

alphabet.add(a[0][0])
dfs(0, 0, 1)

print(result)
