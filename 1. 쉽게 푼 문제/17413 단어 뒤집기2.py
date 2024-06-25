from collections import deque

s = input()
d = deque()
flag = False

for i in s:
    if i == '<':
        flag = True
        
        if d:               
            while d:
                print(d.pop(), end = '')

        d.append(i)
    elif i == '>':
        flag = False
        d.append(i)
        
        while d:
            print(d.popleft(), end = '')
    elif i == ' ':
        if flag: # 태그 내부 공백의 경우
            d.append(i)
        else: # 태그 외부 공백의 경우
            while d:
                print(d.pop(), end = '')

            print(' ', end ='')
    else:
        d.append(i)

while d:
    print(d.pop(), end = '')
