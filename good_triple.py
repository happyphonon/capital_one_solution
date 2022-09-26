'''
是找出一个数组的good triple有多少个。good triple定义就是相邻三个数，
其中两个相加等于另外一个就算good triple。元素可以重复。
'''
def is_good_triple(a, b, c):
    return a + b == c or a + c == b or b + c == a

def solution(arr):
    num_good_triple = 0
    if len(arr) < 3:
        return num_good_triple
    for i in range(2, len(arr)):
        if is_good_triple(arr[i-2], arr[i-1], arr[i]):
            num_good_triple += 1
    return num_good_triple

print(solution([1, 2, 3, 0, 3, 1, 4]))

print(solution([1, 4, 5, 9, 13, 4, 9]))