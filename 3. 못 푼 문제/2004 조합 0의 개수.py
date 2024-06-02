# 숫자의 끝자리가 0이 되려면 그 숫자가 10으로 나누어떨어져야 함
# 10은 2와 5의 곱이므로, 끝자리에 0이 형성되려면 해당 숫자가 2와 5의 쌍을 포함해야 함

def count(n, k):
    count = 0
    original_k = k
    
    while n >= k:
        count += n // k
        k *= original_k
        
    return count
# ex) 8! 내 2의 개수는?
# 2의 배수의 수 = 4 (2, 4, 6, 8)
# 4의 배수의 수 = 2 (4, 8)
# 8의 배수의 수 = 1 (8)
# 4 + 2 + 1 = 7

n, m = map(int, input().split())
two_count = count(n, 2) - count(n - m, 2) - count(m, 2)
five_count = count(n, 5) - count(n - m, 5) - count(m, 5)
# nCm = n! / m! * (n - m)!
# nCm 내 2의 개수 = n! 내 2의 개수 - m! 내 2의 개수 - (n - m)! 내 2의 개수

print(min(two_count, five_count))
