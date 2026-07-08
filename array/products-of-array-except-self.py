# First try wrong answer

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        awk = 0
        for i in nums:
            total*=i
        res = []
        for i in nums:
            if i == 0:
                # no idea what to do
            else:
                res.append(total//i)
        return res

# Prefix Postfix Approach

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        x = [1] * len(nums)
        for i in range(len(nums)):
            x[i]=p
            p*=nums[i]
        p = 1
        for i in range(len(nums)-1, -1, -1):
            x[i]*=p
            p*=nums[i]
        return x
