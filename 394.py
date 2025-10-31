class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        res = ""

        for c in s:
            if c == ']':
                tmp_num , tmp_res = stack.pop()
                res = tmp_res + tmp_num * res
            elif c == '[':
                stack.append([num, res])
                num = 0
                res = ""
            elif  '0' <= c <= '9':
                num = num * 10 + int(c)
            else:
                res += c 
        return res