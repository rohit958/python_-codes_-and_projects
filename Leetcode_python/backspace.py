def backspaceCompare( s: str, t: str) -> bool:
    stack1 = []
    for x in range(len(s)):
        if s[x] == '#':
            stack1.pop()
        else:
            stack1.append(s[x])

    stack2 = []
    for y in range(len(t)):
        if t[y] == '#':
            stack2.pop()
        else:
            stack2.append(t[y])
    if stack1 == stack2:
        return True
    else:
        return False

s = "ab#c"

t = "ad#c"
print(backspaceCompare(s,t))