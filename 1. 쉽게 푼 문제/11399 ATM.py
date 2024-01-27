n = int(input())
a = sorted(list(map(int, input().split())))
tmp = 0
result = 0

for i in a:
    tmp += i
    result += tmp

print(result)
