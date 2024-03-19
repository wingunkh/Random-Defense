import sys
sys.setrecursionlimit(10 ** 6)

def find(a):
    if a == parent[a]:
        return parent[a]
    else:
        return find(parent[a])

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
truth = list(map(int, input().split()))
truth.pop(0)
party = []
result = 0

for _ in range(m):
    buff = list(map(int, input().split()))
    buff.pop(0)
    party.append(buff)

    for i in range(len(buff) - 1):
        union(buff[i], buff[i + 1])

for i in party:
    for j in truth:
        if find(i[0]) == find(j):
            break
    else:
        result += 1

print(result)
