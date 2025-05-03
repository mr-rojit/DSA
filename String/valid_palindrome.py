"""
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

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

def isPalindrome(s: str) -> bool:
    st , end = 0, len(s) -1
    
    while st<=end:
        if not s[st].isalnum():
            st +=1
        elif not s[end].isalnum():
            end -=1
        else:
            if s[st].lower() != s[end].lower():
                return False
            st +=1
            end -=1
    return True
            
        
    
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))