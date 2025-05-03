"""
852. Peak Index in a Mountain Array
You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

Return the index of the peak element.

Your task is to solve it in O(log(n)) time complexity.


Example 1:

Input: arr = [0,1,0]

Output: 1

Example 2:

Input: arr = [0,2,1,0]

Output: 1

"""

def find_peak_index(arr):
    s , e = 0, len(arr)-1
    
    
    while s <= e:
    
        mid = (s+e) // 2
        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return mid
        elif arr[mid] > arr[mid+1]:
            e = mid - 1
        else:
            s = mid + 1
    
            

    


nums = [3,9,8,6,4]
idx = find_peak_index(nums)
print(idx)