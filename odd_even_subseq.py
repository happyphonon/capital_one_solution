'''
给一个整数数组，找出奇偶交替数列总个数，比如说[1,2,5],
符合要求的奇偶交替连续subsequence是[1], [1,2], [2], [2,5], [5], [1,2,5], 总共是6个,
就返回6
'''
count = 0

class Solution():

    def __init__(self):
        self.count = 0

    def dfs(self, arr, flag):
        if len(arr) == 0:
            return
        if flag and (arr[0] % 2 == 1):
            self.count += 1
            self.dfs(arr[1:], not flag)
        if (not flag) and (arr[0] % 2 == 0):
            self.count += 1
            self.dfs(arr[1:], not flag)

    def find_even_odd_subsequence(self, arr):
        if len(arr) == 0:
            return self.count
        
        for i in range(len(arr)):
            flag = arr[i] % 2 == 0
            self.count += 1
            self.dfs(arr[i+1:], flag)
        return self.count

solver = Solution()
print(solver.find_even_odd_subsequence([1, 2, 5]))