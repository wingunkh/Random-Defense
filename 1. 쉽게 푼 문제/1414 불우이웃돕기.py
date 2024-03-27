import sys
sys.setrecursionlimit(10 ** 6)

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
edges = []
parent = [i for i in range(n)]
sum, count, result = 0, 0, 0

for i in range(n):
    s = input()

    for j in range(n):
        length = 0

        if s[j] == '0':
            continue
        elif 'a' <= s[j] <= 'z':
            length = ord(s[j]) - ord('a') + 1
        else:
            length = ord(s[j]) - ord('A') + 27

        sum += length

        if i != j:
            edges.append((i, j, length))

edges.sort(key = lambda x: x[2])

for s, e, w in edges:
    s = find(s)
    e = find(e)

    if s == e:
        continue

    union(s, e)
    count += 1
    result += w

if count != n - 1:
    print(-1)
else:
    print(sum - result)
