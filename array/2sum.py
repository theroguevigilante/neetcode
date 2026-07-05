class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}
        for i, value in enumerate(nums):
            if target - value in x:
                return [x[target - value], i]
            x[value] = i
        return []
