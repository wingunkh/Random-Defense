n = int(input())
a = [list(map(int, input().split())) for _ in range(6)]
bigr, bigr_index = 0, 0
bigc, bigc_index = 0, 0

for i in range(6):
    if a[i][0] == 1 or a[i][0] == 2:
        if a[i][1] > bigr:
            bigr = a[i][1]
            bigr_index = i

    if a[i][0] == 3 or a[i][0] == 4:
        if a[i][1] > bigc:
            bigc = a[i][1]
            bigc_index = i

smallr = abs(a[(bigr_index - 1) % 6][1] - a[(bigr_index + 1) % 6][1])
smallc = abs(a[(bigc_index - 1) % 6][1] - a[(bigc_index + 1) % 6][1])

print((bigr * bigc - smallr * smallc) * n)
