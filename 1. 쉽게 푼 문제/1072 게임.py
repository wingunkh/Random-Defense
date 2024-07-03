import sys
from decimal import Decimal

game, win = map(int, input().split())
rate = int(Decimal(win) / Decimal(game) * 100)
left = 0
right = sys.maxsize
result = sys.maxsize

while left <= right:
    center = (left + right) // 2

    if int(Decimal(win + center) / Decimal(game + center) * 100) > rate:
        result = min(result, center)
        right = center - 1
    else:
        left = center + 1

if result == sys.maxsize:
    print(-1)
else:
    print(result)
