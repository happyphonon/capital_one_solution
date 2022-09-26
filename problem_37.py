'''
给一个数字 n, 算一下包括n在内 0, 2, and 4 出现了多少次. 举例:n = 10, 
solution(n)=4, n = 22,solution(n) = 11
answer: https://blog.csdn.net/u013700358/article/details/90750774
'''

def check(n, d):
    res = 0
    while n:
        if n % 10 == d:
            res += 1
        n //= 10
    return res

def count(n, d):
    if n < 10:
        return int(d > 0 and n >= d)
    if n % 10 != 9:
        return check(n, d) + count(n - 1, d)
    return 10 * count(n // 10, d) + n // 10 + int(d > 0)

def solution(n):
    return 1 + count(n, 0) + count(n, 2) + count(n, 4)

print(solution(10))
print(solution(22))