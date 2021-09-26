# Find the substring

def firstOccurrence(s, x):
    # Write your code here
    t = 0
    i = 0
    
    for i in range(len(s)):
        if t == len(x):
            break
        if s[i] == x[t] or (s[i] and x[t] == "*"):
            t += 1
        else:
            t = 0
    
    if t < len(x):
        return -1
    else:
        return (i - t)

s = "juliasamanthantjulia"
x = "ant"
firstOccurrence(s,x)
