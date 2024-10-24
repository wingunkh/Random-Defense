n, x, y = map(int, input().split())
result = 0

while x != y:
    x = (x + 1) // 2
    y = (y + 1) // 2
    result += 1

print(result)
