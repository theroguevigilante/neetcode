# Can be done with sorting but sorting takes O(nlogn) so HashSet is a better approach

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x = set(nums)
        l = 0
        for i in x:
            curr = 1
            while i - 1 in x:
                curr+=1
                i = i - 1
            l = max(curr, l)
        return l
