import sys

n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))
target = sys.maxsize
result = 0

for i in range(n - 1):
    target = min(target, cost[i])
    result += distance[i] * target

print(result)
