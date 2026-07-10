class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                ct, ci = stack.pop()
                res[ci] = (i - ci)
            stack.append([val, i])
        return res
