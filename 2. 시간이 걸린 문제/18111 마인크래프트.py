import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
height = [0 for _ in range(257)]  # height[i] = 높이가 i인 블록의 수
result_time, result_height = sys.maxsize, 0

for r in range(n):
    for c in range(m):
        height[a[r][c]] += 1

for h in range(257):
    need = 0
    time = 0
    
    for i in range(257):
        if i < h:
            need += (h - i) * height[i]
            time += (h - i) * height[i]
        elif i > h:
            need -= (i - h) * height[i]
            time += 2 * (i - h) * height[i]
    
    if need > b:
        continue

    if time <= result_time:
        result_time = time
        result_height = h

print(result_time, result_height)
