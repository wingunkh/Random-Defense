stick = [64]
x = int(input())

while True:
    stick_sum = sum(stick)

    if stick_sum == x:
        print(len(stick))
        break

    stick[-1] //= 2

    if stick_sum - stick[-1] < x:
        stick.append(stick[-1])
