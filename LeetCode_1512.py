# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         ans = 0
#         for i in range(0, len(nums) - 1):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] == nums[j]:
#                     ans+=1
        
#         return ans
class Solution:
    def numIdenticalPairs(self, nums):
        return int(sum(k * (k -1)/2 for k in collections.Counter(nums).values()))
    
    ### collections -- container types, here we learn the "Counter" objects, it will give us a dictionary: 
    ### key will be the unique elements of the input
    ### value will be the number of each key