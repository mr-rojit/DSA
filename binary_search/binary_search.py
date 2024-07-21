
def binary_search(arr, item):
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


arr = [1,3,5,7,14,16,19]

idx = binary_search(arr, 31)

print(idx)