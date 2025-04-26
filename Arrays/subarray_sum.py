
def get_subarray_sum_opt(arr):
    n = len(arr)
    ans = -100
    for s in range(n-1):
        running_sum = 0
        for e in range(s+1, n):
            ...
            
            

def get_subarray_sum(arr):
    """
    n^3 program to find max sub array sum
    """
    n = len(arr)
    ans = 0
    for i in range(n):
        for j in range(i+1, n+1):
            s = 0
            for k in range(i, j):
                # print(arr[k], end=" ")
                s += arr[k]
            ans = max(ans, s)
            # print()
    return ans


def kadane_algo(arr):
    n = len(arr)
    s = -200
    running_sum = 0
    for i in range(n):
        running_sum += arr[i]
        s = max(s, running_sum)
        if running_sum < 0:
            running_sum = 0
    return s
    

if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    
    # s = get_subarray_sum(arr)
    # s = get_subarray_sum_opt(arr)
    s = kadane_algo(arr)
    print(s)