import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))
start = 0
end = m - 1
window = sum(a[start : end + 1])
result = -sys.maxsize

while True:
    result = max(result, window)
    
    start += 1
    end += 1
    
    if end == len(a):
        break

    window -= a[start - 1]
    window += a[end]

print(result)
