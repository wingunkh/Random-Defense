import sys
sys.setrecursionlimit(10 ** 6)

def dfs(v):
    global result
    count = 0
    
    for i in a[v]:
        if i != target:
            count += 1
            dfs(i)

    if count == 0:
        result += 1

n = int(input())
buff = list(map(int, input().split()))
target = int(input())
a = [[] for _ in range(n)]
root = 0
result = 0

for i in range(n):
    if buff[i] == -1:
        root = i
        continue

    a[buff[i]].append(i)

if target == root:
    print(0)
else:
    dfs(root)
    print(result)
