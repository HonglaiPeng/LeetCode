class Solution(object):
    def buildArray(self, nums):
        ans = []
        for i in range(len(nums)):
            k = nums[nums[i]]
            ans.append(k)
            
        return ans