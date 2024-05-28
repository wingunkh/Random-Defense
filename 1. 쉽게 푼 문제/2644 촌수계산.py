def dfs(x, depth):
    global result
    
    if x == target2:
        result = depth
        
        return
    
    visited[x] = True

    for i in a[x]:
        if not visited[i]:
            dfs(i, depth + 1)

n = int(input())
target1, target2 = map(int, input().split())
m = int(input())
a = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
result = -1

for _ in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)

dfs(target1, 0)

print(result)
