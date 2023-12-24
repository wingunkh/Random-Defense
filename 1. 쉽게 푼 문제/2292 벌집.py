n = int(input())
result = 1
count = 1

while n > 1:
    n -= 6 * count
    result += 1
    count += 1

print(result)
