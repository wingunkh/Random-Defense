# 이분 그래프 : 그래프의 정점의 집합을 둘로 나눴을 때,
# 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있는 그래프

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(v, color):
    global answer
    
    visited[v] = color

    for i in a[v]:
        if not visited[i]:
            dfs(i, -color) # 인접 노드는 같은 집합이 아니므로 다른 집합으로 처리
        elif visited[i] == visited[v]:
            answer = False

t = int(input())

for _ in range(t):
    v, e = map(int, input().split())
    a = [[] for _ in range(v + 1)]
    visited = [0 for _ in range(v + 1)]
    answer = True

    for _ in range(e):
        s, e = map(int, input().split())
        a[s].append(e)
        a[e].append(s)

    for i in range(1, v + 1):
        if answer:
            if not visited[i]:
                dfs(i, -1)
        else:
            print("NO")
            break
    else:
        print("YES")
