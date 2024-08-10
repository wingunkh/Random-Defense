n = 1000 - int(input())
coin = [500, 100, 50, 10, 5, 1]
result = 0

for i in coin:
    result += n // i
    n %= i

print(result)
