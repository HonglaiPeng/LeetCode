# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         ans = []
#         for i in range(0, len(nums)):
#             k = 0
#             for j in range(0, len(nums)):
#                 if(nums[i] > nums[j]):
#                     k+=1
#             ans.append(k)
#         return ans

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        indices = {}
        for idx, num in enumerate(sorted(nums)): ## Enumerate() method adds a counter to an iterable 
                                                 ##                and returns it in a form of enumerating object. 
                                                 ##This enumerated object can then be used directly for loops or converted into a list of tuples 
                                                 ##using the list() method.
            indices.setdefault(num, idx)
            print(num, idx)
        print(indices)
        return [indices[num] for num in nums]