"""
max sub array of size k
"""

def maxSubArray(nums, k):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    max_sum = float('-inf')
    current_sum = 0

    for i in range(n):
        current_sum += nums[i]
        if i >= k-1:
            if current_sum > max_sum:
                max_sum = current_sum
            current_sum -= nums[i - k + 1]
    return max_sum
            

k = 3
nums = [4,2,1,7,8,1,2,8,1,0]

largest_sum = maxSubArray(nums, k)
print(largest_sum)