import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def find(a):
    if a == parent[a]:
        return parent[a]
    else:
        parent[a] =  find(parent[a])

        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a
        result[a] += result[b]

t = int(input())

for _ in range(t):
    n = int(input())
    parent = dict()
    result = dict()

    for _ in range(n):
        a, b = input().split()

        if a not in parent:
            parent[a] = a
            result[a] = 1

        if b not in parent:
            parent[b] = b
            result[b] = 1

        union(a, b)

        print(result[find(a)])
