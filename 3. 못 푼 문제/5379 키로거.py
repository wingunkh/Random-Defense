t = int(input())

for _ in range(t):
    s = input()
    l = [] # 커서 왼쪽
    r = [] # 커서 오른쪽

    for i in s:
        if i == '-':
            if l:
                l.pop()
        elif i == '<':
            if l:
                r.append(l.pop())
        elif i == '>':
            if r:
                l.append(r.pop())
        else:
            l.append(i)
            
    l.extend(reversed(r))
    print(''.join(l))
