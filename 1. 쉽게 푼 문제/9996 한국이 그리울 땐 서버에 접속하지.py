n = int(input())
pattern = input()
left, right = pattern.split('*')

for _ in range(n):
    a = input()

    if len(a) < len(left) + len(right):
        print("NE")
    elif a[:len(left)] == left and a[-len(right):] == right:
        print("DA")
    else:
        print("NE")
