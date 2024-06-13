import sys
from collections import deque
input = sys.stdin.readline

wheel = [[]]

for _ in range(4):
    wheel.append(deque(list(map(int, input().rstrip()))))

n = int(input())
result = 0

for _ in range(n):
    target, direction = map(int, input().split())
    change = [] # (회전해야 할 톱니바퀴 번호, 회전 방향)을 저장할 리스트
    change.append((target, direction))

    tmp = direction
    
    for i in range(target - 1, 0, -1): # 왼쪽 톱니바퀴 중 회전해야 할 톱니바퀴 선정
        if wheel[i + 1][6] != wheel[i][2]:
            tmp = -tmp
            change.append((i, tmp))
        else:
            break

    tmp = direction

    for i in range(target + 1, 5, 1): # 오른쪽 톱니바퀴 중 회전해야 할 톱니바퀴 선정
        if wheel[i - 1][2] != wheel[i][6]:
            tmp = -tmp
            change.append((i, tmp))
        else:
            break
        
    for number, direction in change:
        if direction == 1: # 시계 방향 회전
            wheel[number].appendleft(wheel[number].pop())
        else: # 반시계 방향 회전
            wheel[number].append(wheel[number].popleft())

if wheel[1][0] == 1:
    result += 1

if wheel[2][0] == 1:
    result += 2

if wheel[3][0] == 1:
    result += 4

if wheel[4][0] == 1:
    result += 8

print(result)
