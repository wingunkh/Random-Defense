import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def calculate(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def find(a):
    if a == parent[a]:
        return parent[a]
    else:
        parent[a] = find(parent[a])
        
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a

n = int(input())
a = []
edges = []
parent = [i for i in range(n + 1)]
result = 0

for _ in range(n):
    x, y = map(float, input().split())
    a.append((x, y))

for i in range(n):
    for j in range(i + 1, n):
        distance = calculate(a[i][0], a[i][1], a[j][0], a[j][1])
        edges.append((i + 1, j + 1, distance))

edges.sort(key = lambda x: x[2])

for start, end, distance in edges:
    if find(start) == find(end):
        continue

    union(start, end)

    result += distance

print(round(result, 2))
