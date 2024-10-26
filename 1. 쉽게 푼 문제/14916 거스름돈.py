n = int(input())
result = 0

while n % 5 != 0 and n >= 2:
    n -= 2
    result += 1

if n % 5 == 0:
    result += n // 5
    print(result)
else:
    print(-1)
