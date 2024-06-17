import sys
from copy import deepcopy

def backtracking(x, depth):
    global result
    
    if depth == 3:
        archor = []
        
        for i in range(m):
            if visited[i]:
                archor.append(i)

        result = max(result, simulate(deepcopy(a), archor))

        return

    for i in range(x, m):
        if not visited[i]:
            visited[i] = True
            backtracking(i + 1, depth + 1)
            visited[i] = False

def simulate(a, archor):
    count = 0

    while True:
        end = True
        
        for i in archor:
            target_r, target_c = -1, -1
            target_distance = sys.maxsize

            for r in range(n): # 괴물 탐색
                for c in range(m):
                    if a[r][c] == 1 or a[r][c] == -1:
                        distance =  abs(r - n) + abs(c - i)

                        if distance <= d:
                            if distance < target_distance or distance == target_distance and c < target_c:
                                target_r, target_c = r, c
                                target_distance = distance

            if target_distance != sys.maxsize: # 괴물 사살
                a[target_r][target_c] = -1

        for r in range(n): # 죽은 괴물 제외 처리
            for c in range(m):
                if a[r][c] == -1:
                    a[r][c] = 0
                    count += 1

        for r in range(n - 1, -1, -1): # 생존 괴물 이동 처리
            for c in range(m):
                if a[r][c] == 1:
                    a[r][c] = 0

                    if r + 1 < n:
                        a[r + 1][c] = 1

        for r in range(n): # 종료 조건 검사
            for c in range(m):
                if a[r][c] == 1:
                    end = False

        if end:
            return count
        
n, m, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(m)]
result = 0

backtracking(0, 0)

print(result)
