def dfs(r, depth): # 사다리 설치
    global result

    if check():
        result = min(result, depth)

        return
    
    if depth == 3:
        return

    for i in range(r, h + 1):
        for j in range(1, n):
            if a[i][j] == 0:
                if j >= 1 and a[i][j - 1] == 1: # 왼쪽에 사다리가 있을 경우
                    continue
 
                if a[i][j + 1] == 1: # 오른쪽에 사다리가 있을 경우
                    continue
                
                a[i][j] = 1
                dfs(i, depth + 1)
                a[i][j] = 0

def check(): # 사다리 순회
    for i in range(1, n + 1):
        now = i

        for r in range(1, h + 1):
            if a[r][now]: # 오른쪽에 사다리가 있을 경우
                now += 1
            elif now - 1 >= 0 and a[r][now - 1]: # 왼쪽에 사다리가 있을 경우
                now -= 1

        if now != i:
            return False
    else:
        return True

n, m, h  = map(int, input().split())
a = [[0 for _ in range(n + 1)] for _ in range(h + 1)]
result = 4

for _ in range(m):
    x, y = map(int, input().split())
    a[x][y] = 1
    # a[x][y] = y번 세로선과 y + 1번 세로선을 연결하는 x번 가로선의 존재 유무 

dfs(1, 0)

if result == 4:
    print(-1)
else:
    print(result)
