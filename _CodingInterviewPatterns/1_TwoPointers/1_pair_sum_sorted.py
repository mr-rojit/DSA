"""
Given an array of integers sorted in ascending order and a target value, return the index
of any pair of numbers in the array that sum to the tar-get. The order of the indexes In the
result doesn't matter. If no pair is found, return an empty array.
Excample 1:

1 Input nums ( -5, -2, 3, 4, 6), target = 7
Output = (2, 3)
Explanation: nums[2] + nums[3] = 3 + 4 = 7

Example 2:
Input nums = [1, 1, 1], target = 2
Output: (0, 1)
Explanation: Either valid outputs could be [ 1, 0], [ 0, 2] , [ 2, 0] , [ 1, 2] or [2, 1]
"""

def pair_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def pair_sum_two_pointers(nums, target):
    s, e = 0, len(nums)-1
    
    while s < e:
        sm = nums[s] + nums[e]
        if sm == target:
            return [s, e]
        elif sm < target:
            s +=1
        else:
            e -= 1
    return []
        



nums = [-5, -2, 3, 4, 6]
target = 7
# idx = pair_sum_brute_force(nums, target)
idx = pair_sum_two_pointers(nums, target)

print(idx)