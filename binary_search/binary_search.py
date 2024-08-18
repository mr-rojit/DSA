
def binary_search_iterative(arr, item):
    n = len(arr)
    low, high = 0, n-1

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            high = mid -1
        else:
            low = mid + 1
    return -1



def binary_search_recursive(arr, item, low, high):

    mid = (high + low) //2

    if low > high:
        return -1
    
    if arr[mid] == item:
        return mid
    elif arr[mid] > item:
        return binary_search_recursive(arr, item, low, mid-1)
    else:
        return binary_search_recursive(arr, item, mid+1, high)
    



arr = [1,3,5,7,14,16,19]

# idx = binary_search_iterative(arr, 3)

idx = binary_search_recursive(arr, 19, 0, len(arr)-1)

print(idx)