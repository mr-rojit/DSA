def check_array_sorted(nums,idx, n):
    
    if n <=1:
        return True
    
    if idx >= n:
        return True
    if nums[idx] >= nums[idx-1]:
        return check_array_sorted(nums, idx+1, n)
    else:
        return False
    


nums =  [1,3,5,8,19,37,56]
print(check_array_sorted(nums, 1, len(nums)))