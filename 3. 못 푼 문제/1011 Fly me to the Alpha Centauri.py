import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    target = y - x
    result = 0
    tmp = 0
    distance = 0

    while distance < target:
        result += 1

        if result % 2 == 1:
            tmp += 1

        distance += tmp

    print(result)
