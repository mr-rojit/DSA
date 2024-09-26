"""
Given an array of integers and a number k, find the maximum sum of a subarray of size k. 
Examples: 

    Input  : arr[100, 200, 300, 400],  k = 2
    Output : 700

    Input  : arr[1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4 
    Output : 39
    Explanation: We get maximum sum by adding subarray [4, 2, 10, 23] of size 4.

    Input  : arr[2, 3], k = 3
    Output : Invalid
    Explanation: There is no subarray of size 3 as size of whole array is 2. 
"""

def maximum_sum_of_size_k(arr, k):
    n = len(arr)
    if n < k:
        return "Invalid"
    max_sum = -10 # should be INT MIN
    running_sum = 0

    for i in range(n):
        running_sum += arr[i]
        if i >= k-1: # 2
            max_sum = max(max_sum, running_sum)
            running_sum -= arr[i-k+1]
    return max_sum


arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4

max_sum = maximum_sum_of_size_k(arr, k)
print(max_sum)