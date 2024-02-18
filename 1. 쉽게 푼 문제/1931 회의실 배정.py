import sys
input = sys.stdin.readline

n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]
end = 0
result = 0

a.sort(key = lambda x: (x[1], x[0]))

for i in a:
    if i[0] >= end:
        end = i[1]
        result += 1

print(result)
