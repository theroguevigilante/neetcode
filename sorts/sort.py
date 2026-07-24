from typing import List

class Solution:
    @staticmethod
    def merge_sort(arr: List[int]):
        def merge(a1: List[int], a2: List[int]):
            i, j = 0, 0
            temp = []
            while i < len(a1) and j < len(a2):
                if a1[i] > a2[j]:
                    temp.append(a2[j])
                    j+=1
                else:
                    temp.append(a1[i])
                    i+=1
            while i < len(a1):
                temp.append(a1[i])
                i+=1
            while j < len(a2):
                temp.append(a2[j])
                j+=1
            return temp

        if len(arr) < 2:
            return arr
        mid = len(arr) //  2
        a1 = Solution.merge_sort(arr[:mid])
        a2 = Solution.merge_sort(arr[mid:])

        return merge(a1, a2)

    @staticmethod
    def bubble_sort(arr: List[int]):
        for i in range(len(arr)):
            swapped = False
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                break

    @staticmethod
    def insertion_sort(arr: List[int]):
        for i in range(1, len(arr)):
            for j in range(i, 0, -1):
                if arr[j] < arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
                else:
                    break

    @staticmethod
    def selection_sort(arr: List[int]):
        for i in range(len(arr)):
            curr_min = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[curr_min]:
                    curr_min = j
            arr[curr_min], arr[i] = arr[i], arr[curr_min]

if __name__ == "__main__":
    arr = [23, 12, 32, 16, 88, 78, 94]
    Solution.selection_sort(arr)
    print(arr)
