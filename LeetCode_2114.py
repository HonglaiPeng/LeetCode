# class Solution(object):
#     def mostWordsFound(self, sentences):
#         """
#         :type sentences: List[str]
#         :rtype: int
#         """
#         ans = 0
#         if len(sentences) == None:
#             return ans
#         for sen in sentences:
#             temp = 0
#             for i in range (0, len(sen)):
#                 if sen[i] == " ":
#                     temp += 1
#                 if ans < temp:
#                     ans = temp
        
#         return ans + 1

# class Solution:
#     def mostWordsFound(self, sentences: List[str]) -> int: 
#         return max([len(i.split()) for i in sentences])

    
class Solution:
    def mostWordsFound(self, ss: List[str]) -> int: ## -> here means we need return an int type result
        return max(s.count(" ") for s in ss) + 1