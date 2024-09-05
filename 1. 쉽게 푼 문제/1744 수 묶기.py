n = int(input())
a = [int(input()) for _ in range(n)]
plus = []
zero = []
minus = []
result = 0

for i in a:
    if i > 0:
        plus.append(i)
    elif i == 0:
        zero.append(i)
    else:
        minus.append(i)

plus.sort(reverse = True) # 4 3 2 1
minus.sort() # -4 -3 -2 -1

if len(plus) % 2 == 1:
    result += plus.pop(-1)

if len(minus) % 2 == 1:
    if len(zero) > 0:
        minus.pop(-1)
    else:
        result += minus.pop(-1)

for i in range(0, len(plus) - 1, 2):
    result += max(plus[i] + plus[i + 1], plus[i] * plus[i + 1])

for i in range(0, len(minus) - 1, 2):
    result += max(minus[i] + minus[i + 1], minus[i] * minus[i + 1])

print(result)
