"""

Given a set of positive integers and a target sum, find all subsets of the given set that add up to the target sum.

"""

nums = [1,2,3]
target = 3

result = []
def find_subset(start, subset, sum):
    
    if sum == target:
        result.append(list(subset))
        return

    if sum > target:
        return
    
    for i in range(start, len(nums)):

        subset.append(nums[i])
        find_subset(i+1, subset, sum + nums[i])
        subset.pop()


find_subset(0, [], 0)
print(result)

