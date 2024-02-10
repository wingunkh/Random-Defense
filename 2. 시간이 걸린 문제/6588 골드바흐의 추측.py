import sys
input = sys.stdin.readline

a = [i for i in range(1000001)]
a[1] = 0

for i in range(2, int(len(a) ** 0.5) + 1):
    if a[i] == 0:
        continue

    for j in range(i + i, len(a), i):
        a[j] = 0

while True:
    buff = int(input())

    if buff == 0:
        break

    for i in range(3, len(a) // 2 + 1, 2):
        if a[i] and a[buff - i]:
            print(f"{buff} = {i} + {buff - i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")
