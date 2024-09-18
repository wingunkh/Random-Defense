def func():
    left, right = 0, len(s) - 1

    while left <= right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            case1 = s[left:right]
            case2 = s[left + 1:right + 1]

            if case1 == case1[::-1]:
                return True
            elif case2 == case2[::-1]:
                return True
            else:
                return False

t = int(input())

for _ in range(t):
    s = input()

    if s == s[::-1]:
        print(0)
    elif func():
        print(1)
    else:
        print(2)
