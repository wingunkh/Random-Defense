def dfs(x, depth):
    global result

    if depth == k - 5:
        count = 0
        
        for string in target:
            for i in string:
                if not visited[ord(i) - 97]:
                    break
            else:
                count += 1

        result = max(result, count)

        return      
    
    for i in range(x, 26):
        if not visited[i]:
            visited[i] = True
            dfs(i + 1, depth + 1)
            visited[i] = False

n, k = map(int, input().split())
a = [list(input()) for _ in range(n)]
target = []
visited = [False for _ in range(26)]
visited[ord('a') - 97] = True
visited[ord('n') - 97] = True
visited[ord('t') - 97] = True
visited[ord('i') - 97] = True
visited[ord('c') - 97] = True
result = 0

if k < 5:
    print(0)
    exit()

for string in a:
    target.append(string[4:-4])

dfs(0, 0)

print(result)
