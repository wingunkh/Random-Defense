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
m = int(input())
parent = [i for i in range(n + 1)]
result = set()

for i in range(1, n + 1):
    buff = list(map(int, input().split()))

    for j in range(n):
        if buff[j] == 1:
            union(i, j + 1)

target = list(map(int, input().split()))

for i in target:
    result.add(find(i))

if len(result) == 1:
    print("YES")
else:
    print("NO")
