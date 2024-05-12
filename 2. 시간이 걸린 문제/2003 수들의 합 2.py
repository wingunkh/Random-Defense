n, m = map(int, input().split())
a = list(map(int, input().split()))
s = [0]
tmp = 0
left = 1
right = 1
result = 0

for i in a:
    tmp += i
    s.append(tmp)

while right <= n:
    sum = s[right] - s[left - 1]

    if sum == m:
        result += 1
        left += 1
        right += 1
    elif sum > m:
        left += 1

        if left > right:
            right += 1
    else:
        right += 1

print(result)
