class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def splitArray(mid: int) -> bool:
            curr = 0
            subarray = 1
            for n in nums:
                curr+=n
                if curr > mid:
                    curr = n
                    subarray+=1
            return subarray <= k
        l = max(nums)
        r = sum(nums)
        res = r
        while l <= r:
            mid = l + ((r - l) // 2)
            if splitArray(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
