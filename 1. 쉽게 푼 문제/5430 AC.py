from collections import deque

t = int(input())

for _ in range(t):
    buff = input()
    n = int(input())
    a = input()
    q = deque(a[1:-1].split(','))
    reverse = False

    if n == 0:
        q = deque()
    # 입력값이 빈 배열일 때 q = deque([''])
    # 길이가 1이므로 q = deque([])가 되어야 함

    for i in buff:
        if i == 'R':
            reverse = not reverse
        else:
            if not q:
                print("error")
                break
            elif reverse:
                q.pop()
            else:
                q.popleft()
    else:
        if reverse:
            q.reverse()
            print('[' + ','.join(q) + ']')
        else:
            print('[' + ','.join(q) + ']')
