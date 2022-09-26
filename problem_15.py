'''
给你一开始的数字还有一个diff的数列, ex: num= 1500, arr=[100,-200,300] , 
num 要一步一步跟arr加或减, return 最大值跟最后值
'''
def solution(arr, num):
    max = num
    final = num
    for val in arr:
        final += val
        if final > max:
            max = final
    return max, final


print(solution([100, -200, 300], 1500))
print(solution([100, -200, -300], 1500))