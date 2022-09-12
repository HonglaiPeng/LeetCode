class Solution(object):
    def getConcatenation(self, nums):
        n = len(nums)
        for i in range(n):
            nums.append(nums[i])
        return nums
            
        # ans = []
        # for num in nums:
        #     ans.append(num)
        # for num in nums:
        #     ans.append(num)
        # print(type(nums), type(ans))
        # return ans
          