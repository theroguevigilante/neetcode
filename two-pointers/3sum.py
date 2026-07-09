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

# Set based optimizations
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            x = set()
            target = nums[i] * -1
            for j in range(i+1, len(nums)):
                if target - nums[j] in x:
                   res.add((nums[i], target - nums[j], nums[j]))
                else:
                    x.add(nums[j])
        return list(res)

# Two pointer chadness
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r and l:
                curr = nums[l] + nums[r]
                if curr > target:
                    r-=1
                elif curr < target:
                    l+=1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    l+=1
                    r-=1
        return res
