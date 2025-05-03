"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""

def find_first(nums, target):
    s, e = 0, len(nums)-1
    
    while s < e:
        ...

def searchRange(nums, target):
    ...



nums = [5,7,7,8,8,8,8,8,8,10,17,21]
target = 8
ans = searchRange(nums, target)
print(ans)