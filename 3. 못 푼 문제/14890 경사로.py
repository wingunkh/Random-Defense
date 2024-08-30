def func(line):
    used = [False for i in range(n)]
    
    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            continue
        elif line[i] + 1 == line[i + 1]: # 오르막
            for j in range(i, i - m, -1):
                if j < 0 or line[j] != line[i] or used[j]:
                    return False
                
                used[j] = True        
        elif line[i] - 1 == line[i + 1]: # 내리막
            for j in range(i + 1, i + 1 + m):
                if j >= len(line) or line[j] != line[i + 1] or used[j]:
                    return False
                
                used[j] = True
        else:
            return False
    return True

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
result = 0

for row in a:
    if func(row):
        result += 1

cols = [[row[i] for row in a] for i in range(n)]

for col in cols:
    if func(col):
        result += 1

print(result)
