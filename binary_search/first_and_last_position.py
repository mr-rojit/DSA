"""
34. Find First and Last Position of Element in Sorted Array
Medium
Topics
Companies
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


def find_first(arr, item):
    n = len(arr)
    low, high = 0, n-1

    idx = -1

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] == item:
            idx = mid
            high = mid -1
            
        elif arr[mid] > item:
            high = mid -1
        else:
            low = mid + 1
            
    return idx

def find_last(arr, item):
    n = len(arr)
    low, high = 0, n-1

    idx = -1

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] == item:
            idx = mid
            low = mid + 1
            
        elif arr[mid] > item:
            high = mid -1
        else:
            low = mid + 1
            
    return idx

def find_occurence(arr, item):
    first = find_first(arr, item)
    last = find_last(arr, item)
    return [first, last]


arr = [5,7,7,8,8,10]

idxs = find_occurence(arr, 8)

print(idxs)






