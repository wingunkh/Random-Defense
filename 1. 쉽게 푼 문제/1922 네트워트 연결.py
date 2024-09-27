import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

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
m = int(input())
edges = [list(map(int, input().split())) for _ in range(m)]
parent = [i for i in range(n + 1)]
result = 0

edges.sort(key = lambda x: x[2])

for s, e, w in edges:
    s = find(s)
    e = find(e)

    if s == e:
        continue

    union(s, e)
    result += w

print(result)
