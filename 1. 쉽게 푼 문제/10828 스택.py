import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    buff = input().split()

    if buff[0] == "push":
        stack.append(buff[1])
    elif buff[0] == "pop":
        print(stack.pop()) if stack else print(-1)
    elif buff[0] == "size":
        print(len(stack))
    elif buff[0] == "empty":
        print(0) if stack else print(1)
    else:
        print(stack[-1]) if stack else print(-1)
