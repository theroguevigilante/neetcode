from typing import List
import random
class Sorts:
    @staticmethod
    def merge_sort(nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        m = len(nums) // 2
        left_arr = nums[:m]
        right_arr = nums[m:]
        
        Sorts.merge_sort(left_arr)
        Sorts.merge_sort(right_arr)

        l = 0
        r = 0
        k = 0
        while l < len(left_arr) and r < len(right_arr):
            if left_arr[l] < right_arr[r]:
                nums[k] = left_arr[l]
                l+=1
            else:
                nums[k] = right_arr[r]
                r+=1
            k+=1
        while l < len(left_arr):
            nums[k] = left_arr[l]
            l+=1
            k+=1
        while r < len(right_arr):
            nums[k] = right_arr[r]
            r+=1
            k+=1
        return nums

def main():
    nums = [random.randint(0,100) for _ in range(10)]
    print(nums)
    Sorts.merge_sort(nums)
    print(nums)

if __name__=="__main__":
    main()
