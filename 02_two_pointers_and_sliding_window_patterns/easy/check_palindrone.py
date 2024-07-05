"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:

Input: s = "Was it a car or a cat I saw"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

"""

def isPalindrome(s: str) -> bool:
        s = s.replace(" ", '').lower()
        p1, p2 = 0, len(s)-1
        while p1 < p2:
            if s[p1] != s[p2]:
                  return False
            p1+=1
            p2-=1
        return  True

inp = "Was it a car or a cat I saw"
print(isPalindrome(inp))

