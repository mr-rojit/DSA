def search_item(arr, item):
    s, e  = 0, len(arr)-1
    
    while s < e:
        mid = (s+e) // 2
        
        if arr[mid] == item:
            return mid
        if arr[mid] > item:
            e = mid - 1
        else:
            s = mid + 1
    return -1

nums = [1,3,4,6,18,23,47,55]
idx = search_item(nums, 47)
print(idx)