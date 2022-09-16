class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        ans = []
        for candy in candies:
            kid_candy = 0
            kid_candy = candy + extraCandies
            if(kid_candy >= maximum):
                ans.append(True)
            else:
                ans.append(False)
                
        return ans