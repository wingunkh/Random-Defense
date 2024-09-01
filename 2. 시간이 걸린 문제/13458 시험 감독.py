n = int(input())
a = sorted(list(map(int, input().split())))
b, c = map(int, input().split())
result = 0

for i in range(n):
    a[i] -= b
    result += 1

for i in range(n):
    if a[i] <= 0:
        continue
    
    if a[i] % c == 0:
        result += a[i] // c
    else:
        result += a[i] // c + 1

print(result)
