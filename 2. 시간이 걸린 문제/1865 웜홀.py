import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    edges = []
    distance = [sys.maxsize for _ in range(n + 1)]
    negativeCycle = False

    for _ in range(m):
        s, e, w = map(int, input().split())
        edges.append((s, e, w))
        edges.append((e, s, w))

    for _ in range(k):
        s, e, w = map(int, input().split())
        edges.append((s, e, -w))

    for _ in range(n - 1):
        for s, e, w in edges:
            if distance[e] > distance[s] + w:
                distance[e] = distance[s] + w

    for s, e, w in edges:
        if distance[e] > distance[s] + w:
            negativeCycle = True
            break

    if negativeCycle:
        print("YES")
    else:
        print("NO")
