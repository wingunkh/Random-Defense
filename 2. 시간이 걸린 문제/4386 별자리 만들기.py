import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])

        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a

n = int(input())
parent = [i for i in range(n + 1)]
a = []
edges = []
result = 0

for _ in range(n):
    x, y = map(float, input().split())
    a.append((x, y))

for i in range(n - 1):
    for j in range(i + 1, n):
        edges.append((i, j, ((a[i][0] - a[j][0]) ** 2 + (a[i][1] - a[j][1]) ** 2) ** 0.5))

edges.sort(key = lambda x: x[2])

for start, end, weigth in edges:
    start = find(start)
    end = find(end)

    if start == end:
        continue
    
    union(start, end)
    result += weigth

print(round(result, 2))
