from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {s: index for index, s in enumerate(s)}
        nums = 0
        ans = []
        j = dic[s[0]]
        for i in range(len(s)):
            nums+=1
            if dic[s[i]] > j:
                j = dic[s[i]]
            if i == j:
                ans.append(nums)
                nums = 0
        return ans
    
    def partitionLabels_2(self, s: str)-> List[int]:
        ans = []
        last = {}
        l = len(s)
        end = 0
        start = 0
        for i in range(l):
            for j in range(i,l):
                if s[j] == s[i]:
                    last[s[i]] = j
        
        j = last[s[0]]
        for i in range(len(s)):
            nums+=1
            if last[s[i]] > j:
                j = last[s[i]]
            if i == j:
                ans.append(nums)
                nums = 0
        return ans

