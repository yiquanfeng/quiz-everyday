class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        length = len(temperatures)
        ans = [0] * length
        for i in range(length):
            tmp = temperatures[i]
            while stack and tmp > temperatures[stack[-1]]:
                pre_index = stack.pop()
                ans[pre_index] = i - pre_index
            stack.append(i)

        return ans