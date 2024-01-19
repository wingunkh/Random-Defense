import sys
input = sys.stdin.readline

def dfs(x, depth):
    global result
    
    if depth == n // 2:
        tmp1 = 0
        tmp2 = 0
        
        for r in range(n):
            for c in range(n):
                if visited[r] and visited[c]:
                    tmp1 += a[r][c]
                elif not visited[r] and not visited[c]:
                    tmp2 += a[r][c]

        result = min(result, abs(tmp1 - tmp2))

        return

    for i in range(x, n):
        if not visited[i]:
            visited[i] = True
            dfs(i+1, depth+1)
            visited[i] = False
            
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
result = sys.maxsize

dfs(0, 0)

print(result)
