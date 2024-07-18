
def binary_search(arr, item, low, high):
    mid = (low + high) // 2

    if arr[mid] == item:
        return mid
    
    if high < low:
        return -1
    
    if arr[mid] < item:
        return binary_search(arr, item, mid+1, high)
    
    else:
        return binary_search(arr, item, low, mid-1)


arr = [1,4,6,8,14,16,18,23,46,78,98]
item = 8


print(binary_search(arr, item, 0, len(arr)-1))