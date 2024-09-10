def backtracking1(x, current):
    global left_sum

    left_sum.append(sum(current))
    
    for i in range(x, len(left)):
        current.append(left[i])
        backtracking1(i + 1, current)
        current.pop()

def backtracking2(x, current):
    global right_sum

    right_sum.append(sum(current))
    
    for i in range(x, len(right)):
        current.append(right[i])
        backtracking2(i + 1, current)
        current.pop()

n, m = map(int, input().split())
a = list(map(int, input().split()))
left ,right = a[:n // 2], a[n // 2:]
left_sum, right_sum = [], []
stack = []
result = 0

backtracking1(0, [])
backtracking2(0, [])

left_sum.sort()
right_sum.sort(reverse = True)

p1, p2 = 0, 0

while p1 < len(left_sum) and p2 < len(right_sum):
    target_left, target_right = left_sum[p1], right_sum[p2]
    sum = target_left + target_right

    if sum == m:
        t1, t2 = p1, p2

        while t1 < len(left_sum) and left_sum[t1] == target_left:
            t1 += 1

        while t2 < len(right_sum) and right_sum[t2] == target_right:
            t2 += 1
        
        result += (t1 - p1) * (t2 - p2)
        p1, p2 = t1, t2
    elif sum > m:
        p2 += 1
    else:
        p1 += 1

if m == 0:
    result -= 1

print(result)
