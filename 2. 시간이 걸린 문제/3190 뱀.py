from collections import deque

n = int(input())
a = [[0 for _ in range(n)] for _ in range(n)]
snake = deque([(0, 0)])
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
direction = 0
move = []
result = 0

k = int(input())

for _ in range(k):
    r, c = map(int, input().split())
    a[r - 1][c - 1] = 1

l = int(input())

for _ in range(l):
    x, c = input().split()
    move.append((int(x), c))

while True:
    result += 1
    now = snake[-1]
    next = (now[0] + dr[direction], now[1] + dc[direction])
    # 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.

    if not (0 <= next[0] < n and 0 <= next[1] < n):
        print(result)
        break
    # 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
            
    if next not in snake:
        snake.append(next)
    else:
        print(result)
        break
    # 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.

    if a[next[0]][next[1]] == 1: # 만약 이동한 칸에 사과가 있다면,
        a[next[0]][next[1]] = 0 # 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    else: # 만약 이동한 칸에 사과가 없다면,
        snake.popleft() # 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.

    for x, c in move:
        if x == result:
            if c == 'L':
                direction = (direction + 1) % 4
            else:
                direction = (direction - 1) % 4
                # -1 // 4 = -1 (파이썬은 몫에 대해서 내림을 사용)
                # -1 % 4 = 3
            break
