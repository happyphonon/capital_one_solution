'''
making even numbers on the left and odd numbers on the right.(two pointer)
'''
def solution(arr):
    res = [0 for _ in range(len(arr))]
    i, j = 0, len(arr) - 1
    for val in arr:
        if val % 2 == 0:
            res[i] = val
            i += 1
        if val % 2 == 1:
            res[j] = val
            j -= 1
    return res

print(solution([1, 2, 4, 5, 7, 10, 9]))