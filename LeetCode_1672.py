class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        ans = 0
        for cus in accounts:
            temp = 0
            print(type(cus)) ## list type
            for wealth in cus:
                temp = wealth + temp
                print(type(wealth))  ## int type
            if temp > ans:
                ans = temp
        return ans