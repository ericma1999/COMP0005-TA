def balanced_parenthesis(text):
    stack = []
    for c in text:
        if c == '(':
            stack.append(1)
        elif c == ')':
            stack.pop()
    if not stack:
        return True
    else:
        return False


print(balanced_parenthesis("((x*2)+(x-2)) - a[3] / a[10]"))


print(balanced_parenthesis("(((x*2)+(x-2)) - a[3] / a[10]"))