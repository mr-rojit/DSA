"""
Topics
Companies
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false
"""

def sum_of_squared_nums(c):
    for a in range(1,c):
        for b in range(1, c):
            if a**2 + b**2 == c:
                return True
    return False


print(sum_of_squared_nums(5))

