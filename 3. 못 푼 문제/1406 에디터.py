import sys
input = sys.stdin.readline

s1 = list(input().rstrip())
# sys.stdin.readline() 함수는 개행 문자를 포함하는 것에 유의
# sys.stdin.readline().split()의 경우 개행 문자가 공백으로 취급되는 것
s2 = []

for _ in range(int(input())):
    buff = list(input().split())
    
    if buff[0] == 'L':
        if s1:
            s2.append(s1.pop())
    elif buff[0] == 'D':
        if s2:
            s1.append(s2.pop())
    elif buff[0] == 'B':
        if s1:
            s1.pop() 
    else:
        s1.append(buff[1])
        
s1.extend(reversed(s2))

print(''.join(s1))
