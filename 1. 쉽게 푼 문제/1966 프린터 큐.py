from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    buff = list(map(int, input().split()))
    q = deque()
    result = 0
    
    for i in range(n):
        q.append((buff[i], i))

    while q:
        maximum = 0

        for i in q:
            maximum = max(maximum, i[0])
        
        if q[0][0] == maximum:
            result += 1
            
            if q[0][1] == m:
                break
            else:
                q.popleft()
        else:
            q.append(q.popleft())

    print(result)
