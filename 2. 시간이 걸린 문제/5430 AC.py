from collections import deque

t = int(input())

for _ in range(t):
    buff = input()
    n = int(input())
    a = input()
    q = deque(a[1:-1].split(','))
    flag = 0

    if n == 0:
        q = deque()
    # 입력값이 빈 배열일 때 q = deque([''])
    # 길이가 1이므로 q = deque([])가 되어야 함

    for i in buff:
        if i == 'R':
            flag += 1
        else:
            if not q:
                print("error")
                break
            elif flag % 2 == 0:
                q.popleft()
            else:
                q.pop()
    else:
        if flag % 2 == 0:
            print("[" + ','.join(q) + "]")
        else:
            q.reverse()
            print("[" + ','.join(q) + "]")
