n = int(input())
flag = 1

while True:
    if n == 3 or n == 1:
        break
    elif n > 3:
        n -= 3
        flag = -flag
    else:
        n -= 1
        flag = -flag

if flag == 1:
    print("SK")
else:
    print("CY")
