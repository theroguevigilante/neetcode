# Sorting and them Two Sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            x = {}
            target = nums[i] * -1
            for j in range(i+1, len(nums)):
                if target - nums[j] in x:
                   res.append([nums[i], target - nums[j], nums[j]])
                else:
                    x[nums[j]]=j
        return res
