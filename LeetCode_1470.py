class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        x = []
        y = []
        ans = []
        for i in range(0, n):
            x.append(nums[i])
        for j in range(n, 2*n):
            y.append(nums[j])
        print(x)
        print(y) ### range(start, stop) include the start parameter 
                 ### but not include the stop one.
                 
        for k in range(0, n):
            ans.append(x[k])
            ans.append(y[k])
        return ans