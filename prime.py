#给一个数，找出所有小于等于这个数的质数
def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def solution(n):
    res = []
    for i in range(2, n + 1):
        if is_prime(i):
            res.append(i)
    return res

print(solution(10))

print(solution(20))
