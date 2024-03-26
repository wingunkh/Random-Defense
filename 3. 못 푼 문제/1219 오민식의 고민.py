import sys
input = sys.stdin.readline

n, start, end, m = map(int, input().split())
edges = []
money = [-sys.maxsize for _ in range(n)]
# money[i] = i번째 도시에 도착했을 때 가지고 있을 수 있는 돈의 최대 액수

for _ in range(m):
    s, e, w = map(int, input().split())
    edges.append((s, e, -w))

earn = list(map(int, input().split()))

money[start] = earn[start]

for i in range(n - 1):
    for s, e, w in edges:
        if money[s] != -sys.maxsize and money[e] < money[s] + earn[e] + w:
            money[e] = money[s] + earn[e] + w

for s, e, w in edges:
    if money[s] != -sys.maxsize and money[e] < money[s] + earn[e] + w:
        money[e] = sys.maxsize

for i in range(n - 1):
    for s, e, w in edges:
        if money[s] == sys.maxsize:
            money[e] = sys.maxsize

if money[end] == -sys.maxsize:
    print("gg")
elif money[end] == sys.maxsize:
    print("Gee")
else:
    print(money[end])
