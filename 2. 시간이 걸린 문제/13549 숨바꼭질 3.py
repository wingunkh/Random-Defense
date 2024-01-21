import heapq

def bfs():
    q = []
    heapq.heappush(q, (0, n))
    visited[n] = True

    while q:
        now_time, now_x = heapq.heappop(q)
        
        if now_x == k:
            return now_time

        for i in (now_x - 1, now_x + 1, 2 * now_x):
            if 0 <= i <= 100000 and not visited[i]:
                if i == 2 * now_x:
                    heapq.heappush(q, (now_time, i))
                else:
                    heapq.heappush(q, (now_time + 1, i))
                    
                visited[i] = True
        
n, k = map(int, input().split())
visited = [False for _ in range(100001)]

print(bfs())
