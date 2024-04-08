import sys
input = sys.stdin.readline

n = int(input())
s = set()

for _ in range(n):
    buff = input().split()

    if buff[0] == "add":
        s.add(int(buff[1]))
    elif buff[0] == "check":
        if int(buff[1]) in s:
            print(1)
        else:
            print(0)
    elif buff[0] == "remove":
        if int(buff[1]) in s:
            s.remove(int(buff[1]))
    elif buff[0] == "toggle":
        if int(buff[1]) in s:
            s.remove(int(buff[1]))
        else:
            s.add(int(buff[1]))
    elif buff[0] == "all":
        s = set([i for i in range(1, 21)])
    else:
        s = set()
