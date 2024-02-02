n = int(input())
start = 1
end = 1
sum = 1
result = 0

while end <= n:
    if sum == n:
        result += 1
        end += 1
        sum += end
    elif sum < n:
        end += 1
        sum += end
    else:
        sum -= start
        start += 1

print(result)
