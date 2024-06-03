import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())
a = [[0 for _ in range(C)] for _ in range(R)]
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
result = 0

for _ in range(M):
    r, c, speed, direction, size = map(int, input().split())
    a[r - 1][c - 1] = (speed, direction - 1, size)

for c in range(C): # 1. 낚시왕이 오른쪽으로 한 칸 이동한다
    for r in range(R): # 2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 
        if a[r][c]:
            _, _, size = a[r][c]
            result += size
            a[r][c] = 0 # 2. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
            break

    tmp = [[0 for _ in range(C)] for _ in range(R)]
    
    for r in range(R): # 3. 상어가 이동한다.
        for c in range(C):
            if a[r][c]:
                speed, direction, size = a[r][c]
                next_r, next_c = r, c
                
                if direction == 0 or direction == 1:
                    speed = speed % ((R - 1) * 2)
                else:
                    speed = speed % ((C - 1) * 2)

                for _ in range(speed):
                    next_r, next_c = next_r + dr[direction], next_c + dc[direction]

                    if not (0 <= next_r < R and 0 <= next_c < C): # 상어가 이동하려고 하는 칸이 격자판의 경계를 넘는 경우에는 방향을 반대로 바꿔서 속력을 유지한채로 이동한다.
                        next_r, next_c = next_r - dr[direction], next_c - dc[direction]

                        if direction == 0 or direction == 2:
                            direction += 1
                        else:
                            direction -= 1

                        next_r, next_c = next_r + dr[direction], next_c + dc[direction]

                if tmp[next_r][next_c]: # 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다.
                    if size > tmp[next_r][next_c][2]:
                        tmp[next_r][next_c] = (speed, direction, size)
                else:
                    tmp[next_r][next_c] = (speed, direction, size)

    a = tmp
                
print(result)
