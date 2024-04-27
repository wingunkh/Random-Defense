n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse = True)
result = 0

for i in range(n):
    result += a[i] * b[i]

print(result)
