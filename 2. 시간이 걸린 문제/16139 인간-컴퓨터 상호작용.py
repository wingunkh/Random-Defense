import sys
input = sys.stdin.readline

s = input().rstrip()
n = int(input())
prefix_sum = [[0 for _ in range(26)] for _ in range(len(s) + 1)]

for i in range(1, len(s) + 1):
    for j in range(26):
        prefix_sum[i][j] = prefix_sum[i - 1][j]

    prefix_sum[i][ord(s[i - 1]) - 97] += 1
    
for _ in range(n):
    target, start, end = input().split()
    start = int(start) + 1
    end = int(end) + 1
    
    print(prefix_sum[end][ord(target) - 97] - prefix_sum[start - 1][ord(target) - 97])
