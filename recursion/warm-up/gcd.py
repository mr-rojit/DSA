
## code to find gcd using recursion and brute force approach

def fing_gcd_bf(n1, n2, min):

    if min <= 1:
        return 1
    
    if n1 % min == 0 and n2 % min == 0:
        return min
    
    return fing_gcd_bf(n1, n2, min-1)
    
n1 = 12
n2 = 16

# print(fing_gcd_bf(n1, n2, min(n1,n2)))

## code to find gcd using recursion and euclid algorithm

def find_gcd(n1, n2):

    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    
    return find_gcd(n2, n1 % n2)

print(find_gcd(n1, n2))