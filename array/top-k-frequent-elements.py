class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = {}
        y = [ [] for i in range(len(nums) + 1)]
        
        for i in nums:
            if i in x:
                x[i]+=1
            else:
                x[i]=1
        for i, j in x.items():
            y[j].append(i)
        
        z = []
        for i in range(len(nums), 0, -1):
            if len(z)==k:
                return z
            for l in y[i]:
                z.append(l)
        return z
