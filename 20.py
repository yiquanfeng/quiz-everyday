class Solution:
    def isValid(self, s:str) -> bool:
        stack = []
        dic = { ']': '[', '}': '{', ')': '('}
        for i in s:
            if i in dic and stack:
                if stack[-1] == dic[i]: stack.pop(-1)
                else: return False
            else:
                stack.append(i)
        if not stack:
            return True
        else:
            return False