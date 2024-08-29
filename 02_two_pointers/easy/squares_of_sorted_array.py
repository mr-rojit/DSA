"""
Given a sorted array of integers, return a new array containing the squares of each number sorted in non-decreasing order.
Example:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]

"""


def sortedSquares(nums):
        N = len(nums)
        a = [None] * N

        ptr = N-1
        
        left, right = 0, N-1

        while left <= right:

            l2 = nums[left] **2
            r2 = nums[right] ** 2

            if l2 < r2:
                a[ptr] = r2
                right -=1
            else:
                a[ptr] = l2
                left +=1
            ptr -= 1
        return a


print(sortedSquares([-4,-1,0,3,10]))