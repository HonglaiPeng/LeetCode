class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        i = 0
        for num in nums:
            target.insert(index[i], num) ## list.insert(i, ele) i-->indext ele-->element that you want to insert
            i+=1
        return target