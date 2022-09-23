class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create a hash map
        hashmap = Counter()
        # set two pointers
        left = right = 0
        res = 0
        while right < len(s):
            #traverse string and put unique element in hash map
            r = s[right]
            hashmap[r] += 1
            while hashmap[r] > 1: # that means the process of traversing meet two duplicate letters
                l = s[left]
                hashmap[l] -= 1 # we need reduce the value to 1 again
                left += 1 # keep moving left pointer till all values in this map are less or equal to 1
            res = max(res, right - left + 1)
            right += 1
        return res