n, m, x, y, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dice = [0, 0, 0, 0, 0, 0]
order = list(map(int, input().split()))
#   1
# 3 0 2
#   4
#   5
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

for direction in order:
    if not (0 <= x + dr[direction - 1] < n and 0 <= y + dc[direction - 1] < m):
        continue
    
    x += dr[direction - 1]
    y += dc[direction - 1]
    
    if direction == 1: # 동쪽
        dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
    elif direction == 2: # 서쪽
        dice[0], dice[3], dice[5], dice[2] = dice[2], dice[0], dice[3], dice[5]
    elif direction == 3: # 북쪽
        dice[0], dice[1], dice[5], dice[4] = dice[4], dice[0], dice[1], dice[5]
    elif direction == 4: # 남쪽
        dice[0], dice[4], dice[5], dice[1] = dice[1], dice[0], dice[4], dice[5]

    if a[x][y] == 0:
        a[x][y] = dice[5]
    else:
        dice[5] = a[x][y]
        a[x][y] = 0
        
    print(dice[0])
