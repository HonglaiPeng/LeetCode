class Solution(object):
    def finalValueAfterOperations(self, operations):
        ans = 0
        for operation in operations:
            if operation == "--X" or operation == "X--":
                ans-=1
            else:
                ans+=1        
        return ans
    ## if elif else statement, we use "and" "or"