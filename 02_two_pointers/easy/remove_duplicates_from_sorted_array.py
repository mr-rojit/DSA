"""
Given a sorted array, remove the duplicates in-place such that each element appears only once. Return the new length of the array.
    Example:
    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4]
"""


def remove_duplicates(arr):
    
    slow = 0
    count = 0

    for fast in range(1, len(arr)):
        
        if arr[slow] != arr[fast]:
            slow = fast
            count +=1
    return count + 1



nums = [0,0,1,1,1,2,2,3,3,4,5]
print(remove_duplicates(nums))