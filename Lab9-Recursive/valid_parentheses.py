def valid_parentheses(s):
    if s == "":
        return True
    if "()" in s:
        return valid_parentheses(s.replace("()", "", 1))
    return False
    
print (valid_parentheses("(()()(())())"))
print (valid_parentheses("((()())"))
print (valid_parentheses("())()()("))
print (valid_parentheses("(((()))((())))"))
print (valid_parentheses("()()(((())))"))
print (valid_parentheses("()"))