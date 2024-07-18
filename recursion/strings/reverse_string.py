def rev_str(s: str):
    if s == "":
        return s
    return rev_str(s[1:]) + s[0]


s = "Hello"
# print(rev_str(s))


def check_palindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    if s[0] == s[-1]:
        return check_palindrome(s[1:-1])
    else:
        return False



is_palindrome = check_palindrome('appla')
print(is_palindrome)


