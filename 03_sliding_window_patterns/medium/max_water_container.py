"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

"""
# brute force
def find_max_value_bf(arr):

    n = len(arr)
    width, max_ltr = 0, 0

    for i in range(n):
        for j in range(i+1, n):
            width = j - i
            height = min(arr[i], arr[j])
            max_ltr = max(max_ltr, width*height)

    return max_ltr

def find_max_value(arr):
    n = len(arr)
    max_area = 0
    p1, p2 = 0, n-1
    
    while p1 < p2:
        width = p2 - p1
        height = min(arr[p1], arr[p2])
        area = height * width
        max_area = max(max_area, area)
        
        if arr[p1] <= arr[p2]:
            p1+=1
        else:
            p2 -= 1

    return max_area
    


arr = [1,8,6,2,5,4,8,3,7]
print(find_max_value(arr))