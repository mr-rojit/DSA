"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

"""


def is_palindrome(s):
    new_s = ""
    for i in s:
        if i.isalnum():
            new_s = new_s + i.lower()
    p1, p2 = 0, len(new_s) -1

    while p1 <= p2:
        if new_s[p1] != new_s[p2]:
            return False
        p1+=1
        p2-=1
    return True
    


s = "A man, a plan, a canal: Panama"

print(is_palindrome(s))