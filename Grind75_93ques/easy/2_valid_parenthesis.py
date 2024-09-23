"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

"""

def isValid(s):
    match = {
        ")" : "(",
        "}" : "{",
        "]" : "[",
    }

    stack = []

    for i in s:
        if i in ")}]":
            if not stack:
                return False
            last_item = stack.pop()
            if last_item != match[i]:
                return False
        else:
            stack.append(i)

    if not stack:
        return True
    return False
    

is_valid = isValid('()[]{}')
print(is_valid)


