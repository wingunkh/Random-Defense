while True:
    a = sorted(list(map(int, input().split())))

    if sum(a) == 0:
        break
    else:
        if a[0] ** 2 + a[1] ** 2 == a[2] ** 2:
            print("right")
        else:
            print("wrong")
