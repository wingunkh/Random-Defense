import sys
input = sys.stdin.readline

desk, people = map(int, input().split())
time = [int(input()) for _ in range(desk)]
left, right = 1, min(time) * people
result = sys.maxsize

while left <= right:
    center = (left + right) // 2
    tmp = 0

    for i in time:
        tmp += center // i

    if tmp < people:
        left = center + 1
    else:
        result = min(result, center)
        right = center - 1

print(result)
