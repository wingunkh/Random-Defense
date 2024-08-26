from collections import deque

def move():
    global now_r, now_c, now_d, result
    
    while True:
        now_r, now_c = now_r + dr[now_d][0], now_c + dr[now_d][1]
        result += 1

        if not (0 <= now_r < n and 0 <= now_c < n): # 뱀이 벽에 충돌하는 경우
            return

        if a[now_r][now_c] == 1: # 뱀이 자기자신과 충돌하는 경우
            return
        
        if a[now_r][now_c] == 2: # 뱀이 사과를 먹는 경우
            a[now_r][now_c] = 1
            snake.appendleft((now_r, now_c))
        else: # 뱀이 빈칸으로 이동하는 경우
            a[now_r][now_c] = 1
            snake.appendleft((now_r, now_c))
            r, c = snake.pop()
            a[r][c] = 0

        if result in change: # 방향 전환
            if change[result] == 'D':
                now_d = (now_d + 1) % 4
            else:
                now_d = (now_d - 1) % 4

n = int(input()) # 보드의 크기
a = [[0 for _  in range(n)] for _ in range(n)] # 보드
snake = deque() # 뱀
dr = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 뱀 방향 (→, ↓, ←, ↑)
change = {} # 뱀 방향 전환 정보
now_r, now_c, now_d = 0, 0, 0 # 현재 뱀 좌표 및 방향
result = 0 # 게임 진행 시간

a[0][0] = 1 # 뱀 위치 설정
snake.append((0, 0))

for _ in range(int(input())): # 사과 위치 설정
    r, c = map(int, input().split())
    a[r - 1][c - 1] = 2

for _ in range(int(input())): # 뱀 방향 전환 정보 설정
    x, y = input().split()
    change[int(x)] = y

move()

print(result)
