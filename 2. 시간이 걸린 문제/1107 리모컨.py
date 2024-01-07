def possible(channel):
    for i in channel:
        if int(i) not in button:
            return False
    return True

channel = int(input())
n = int(input())
broken = list(map(int, input().split())) if n > 0 else []
button = [i for i in range(10) if i not in broken]
result = abs(100 - channel)

for i in range(1000001):
    if possible(str(i)):
        result = min(result, len(str(i)) + abs(i - channel))

print(result)
