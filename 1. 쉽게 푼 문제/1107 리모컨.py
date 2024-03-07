def possible(channel):
    for i in channel:
        if int(i) not in button:
            return False
    else:
        return True
    
target = int(input())
n = int(input())
broken = list(map(int, input().split())) if n > 0 else []
button = [i for i in range(10) if i not in broken]
left, right = target, target
worst = abs(100 - target)

while left >= 0 or right <= 1000001:
    if left >= 0 and possible(str(left)):
        print(min(worst, len(str(left)) + abs(left - target)))
        break
    elif right <= 1000001 and possible(str(right)):
        print(min(worst, len(str(right)) + abs(right - target)))
        break

    left -= 1
    right += 1
else:
    print(worst)
