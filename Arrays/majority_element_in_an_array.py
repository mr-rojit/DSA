"""
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

def majority_element(nums):
    nums = sorted(nums)
    freq = len(nums)//2
    element = nums[0]
    c = 1
    
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            c+=1
        else:
            element = nums[i]
            c = 1
        
        if c > freq:
            return element
        
def moores_voting_algo(nums):
    item = None
    freq = 0
    
    for i in range(len(nums)):
        if freq == 0:
            item = nums[i]
        if item == nums[i]:
            freq +=1
        else:
            freq-=1
    return item
            
nums = [2,2,1,1,1,2,2]
item = moores_voting_algo(nums)
print(nums)
print(item)