import sys
input = sys.stdin.readline

n = int(input())
maximum = [0, 0, 0]
minimum = [0, 0, 0]

for _ in range(n):
    a = list(map(int, input().split()))
    maximum = [a[0] + max(maximum[:2]), a[1] + max(maximum[:3]), a[2] + max(maximum[1:3])]
    minimum = [a[0] + min(minimum[:2]), a[1] + min(minimum[:3]), a[2] + min(minimum[1:3])]

print(max(maximum), min(minimum))
