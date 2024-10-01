def dfs(v):
    global result
    is_leaf = True
    
    for i in a[v]:
        if i == target:
            continue

        dfs(i)
        is_leaf = False

    if is_leaf:
        result += 1

n = int(input())
tmp = list(map(int, input().split()))
target = int(input())
a = [[] for _ in range(n)]
root = 0
result = 0

for i in range(n):
    if tmp[i] == -1:
        root = i
        continue

    a[tmp[i]].append(i)

if target == root:
    print(0)
else:
    dfs(root)
    print(result)
