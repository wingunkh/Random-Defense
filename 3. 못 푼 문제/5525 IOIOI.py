n = int(input())
m = int(input())
s = input()
cursor, count, result = 0, 0, 0

while cursor <= m - 2:
    if s[cursor:cursor + 3] == "IOI":
        cursor += 2
        count += 1

        if count == n:
            result += 1
            count -= 1
    else:
        cursor += 1
        count = 0
    
print(result)
