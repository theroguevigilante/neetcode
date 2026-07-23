class Solution:
    def search(self, arr: List[int], target: int) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if target == arr[mid]:
                return mid
            elif target > arr[mid]:
                if arr[mid] < target <= arr[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if arr[mid] > target >= arr[l]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
