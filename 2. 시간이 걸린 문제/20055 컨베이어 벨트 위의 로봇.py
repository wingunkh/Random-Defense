from collections import deque

n, k = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque([0 for _ in range(n)])
result = 0

while True:
    result += 1

    # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    belt.appendleft(belt.pop())
    robot.appendleft(robot.pop())
    robot[-1] = 0

    if sum(robot): # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
        for i in range(n - 2, -1, -1):
            if robot[i] and not robot[i + 1]: # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며,
                if belt[i + 1] > 0: # 그 칸의 내구도가 1 이상 남아 있어야 한다.
                    robot[i + 1] = 1
                    robot[i] = 0
                    belt[i + 1] -= 1

        robot[-1] = 0

    # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if not robot[0] and belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1

    # 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다.
    if belt.count(0) >= k:
        break

print(result)
