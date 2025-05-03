"""
Given an array of integers, return all triplets [a, b, c] such that a + b + c = 0. The
solution must not contain duplicate triplets (e.g., [ 1, 2, 3] and [ 2, 3, 1] are considered
duplicate triplets. If no such triptets are found, return an empty array.

Each triplet can be arranged in any order, and the output can be returned in any order.
Example:
Input nums = [0, -1, 2, -3, 1]
Output [ [-3, 1, 2], [-1, 0, 1] ]

"""

def triplet_sum_brute_force(arr):
    n = len(arr)
    ans = set()
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    a = arr[i], arr[j], arr[k]
                    ans.add(tuple(sorted(a)))
    return ans


def pair_sum(arr, s, target):
    e = len(arr)-1
    pairs = []
    while s < e:
        sm = arr[s] + arr[e]
        
        if sm == target:
            pairs.append([arr[s], arr[e]])
            s+=1
            e-=1
        elif sm < target:
            s+=1
        else:
            e -=1
    return pairs

def triplet_sum(arr):
    arr.sort()
    ans = set()
    for i in range(len(arr)-1):
        if arr[i] >=0:
            break
        pairs = pair_sum(arr, i+1, -arr[i])
        for p in pairs:
            p.append(arr[i])
            ans.add(tuple(sorted(p)))
    return ans
        
                  

nums = [0, -1, 2, -3, -3,  1]
# ans = triplet_sum_brute_force(nums)
ans = triplet_sum(nums)

print(ans)