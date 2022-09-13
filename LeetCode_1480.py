class Solution(object):
    def runningSum(self, nums):
        n = len(nums)
        for i in range(1, n):
            temp = nums[i] + nums[i-1]
            nums[i] = temp
        return nums
            
        
        # ans = []
        # ans.append(nums[0])
        # n = len(nums)
        # for i in range(1, n):
        #     temp = nums[i] + ans[i - 1]
        #     ans.append(temp)
        # return ans
        