from typing import List
from itertools import groupby
# class Solution:
#     def groupAnagrams(strs: List[str]) -> List[List[str]]:
#         lst = {}
#         for s in strs:

#             str_count = []  
#             for c in s:
#                 count = ord(c)
#                 str_count.append(count)
#             lst[s] = sum(str_count)
#         print(lst)
#         res = {}
#         for k, v in lst.items():
#             if v not in res:
#                 res[v].append(k)
#         print(res)
#         # return res


# strs = ['ate', 'eat', 'tea', 'tan']
# print(Solution.groupAnagrams(strs=strs))

from heapq import nlargest 
from collections import Counter
# class Solution:
#     def topKFrequent(nums:List[int], k:int) -> List[int]:
#         count = Counter(nums)

#         va = nlargest(k, count, key=count.get)
#         return va 
    
# nums = [1,1,2,2,2,2,3]
# k = 2

# print(Solution.topKFrequent(nums=nums, k=k))


# class Solution:
#     def productExceptSelf(nums=List[int]) -> List[int]:
#         lst = []
#         for n in range(len(nums)):
#             if 
#             for x in nums:
#                 prod = prod * x
#                 lst.append(prod)

#         print(lst)

# nums = [1,2,3,4]
# print(Solution.productExceptSelf(nums=nums))


# def merge_sort(data):
#     if len(data) <= 1:
#         return

#     mid = len(data) / 2
#     left_data = data[:mid]
#     right_data = data[mid:]

    
# def quick_sort(array):
#     less = []
#     equal = []
#     greater = []

#     if len(array) > 1:
#         pivot = array[0]
#         for x in array:
#             if x < pivot:
#                 less.append(x)
#             elif x == pivot:
#                 equal.append(x)
#             else:
#                 greater.append(x)
#             return quick_sort(less)+equal+quick_sort(greater)
#     else:
#         return array


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr, l, r):
            

array = [5,2,3,1]
solution = Solution()
sorted_array = solution.sortArray(array)
print(sorted_array)
  