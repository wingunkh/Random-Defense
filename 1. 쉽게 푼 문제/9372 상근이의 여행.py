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

for _ in range(int(input())):
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    parent = [i for i in range(n + 1)]
    result = 0

    for s, e in edges:
        s = find(s)
        e = find(e)

        if s == e:
            continue

        union(s, e)
        result += 1

    print(result)
