'''
给一个array和pivot,如果array == 0, output = 0,
如果array和pivot同为正或负,output=1,
不同的话output=-1
'''
def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0
    
def solution(array, pivot):
    if array == 0:
        return 0
    if sign(array) * sign(pivot) > 0:
        return 1
    return -1

print(solution(0, -1))
print(solution(0, 1))
print(solution(2, 3))
print(solution(-2, -3))
print(solution(-2, 3))