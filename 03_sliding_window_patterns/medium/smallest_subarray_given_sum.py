
"""

Given an array, return the smallest subarray length whose sum is >= N.

"""

def smallest_subrray_length(arr, N):
    running_sum = 0
    n = len(arr)

    min_sub_array_len = n
    p1 = 0

    for i in range(n):
        running_sum += arr[i]
        
        while running_sum >= N:
            min_sub_array_len = min(min_sub_array_len, i - p1 + 1)
            running_sum -= arr[p1]
            p1+=1
    return min_sub_array_len

                    
    
            


nums = [4,2,2,7,8,1,2,8,10]
N = 8

smallest_subarray_length = smallest_subrray_length(nums, N)
print(smallest_subarray_length)