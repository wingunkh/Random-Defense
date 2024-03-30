t = int(input())
n = int(input())
a = [0] + list(map(int, input().split()))
m = int(input())
b = [0] + list(map(int, input().split()))
dic = {}
result = 0

for i in range(1, n + 1):
    a[i] = a[i] + a[i - 1]

for i in range(1, m + 1):
    b[i] = b[i] + b[i - 1]

for a_right in range(1, n + 1):
    for a_left in range(a_right):
        a_sum = a[a_right] - a[a_left]

        if a_sum not in dic:
            dic[a_sum] = 1
        else:
            dic[a_sum] += 1

for b_right in range(1, m + 1):
    for b_left in range(b_right):
        b_sum = b[b_right] - b[b_left]

        if t - b_sum in dic:
            result += dic[t - b_sum]

print(result)
