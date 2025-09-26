def isParindrome(s):
    s = s.lower()
    # print(s)
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return isParindrome(s[1:-1])


print(isParindrome("abcdcba"))
print(isParindrome("atoyota"))
print(isParindrome("kmitl"))
print(isParindrome("manassanan"))
print(isParindrome("programming"))
print(isParindrome("fundamental"))
