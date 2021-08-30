"""
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
Input: s = "()"
Output: true
"""


def check_valid_string(s):
    lo = hi = 0
    for c in s:
        lo += 1 if c == '(' else -1
        hi += 1 if c != ')' else -1
        if hi < 0:
            break
        lo = max(lo, 0)

    return lo == 0



def check_valid_string_2(self, s):
    stack = []
    for c in s:
        if c in '(*':
            stack.append(c)
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)

    stars = []
    parens = []
    
    for i, c in enumerate(stack):
        if c == '*':
            stars.append((i, c))
        elif c == '(':
            parens.append((i, c))
        else:  # c == ')'
            if parens:
                parens.pop()
            elif stars:
                stars.pop()
            else:
                return False
            
    while parens:
        i, c = parens.pop()
        if not stars:
            return False
        if stars[-1][0] < i:
            return False
        stars.pop()        
    
    return True


