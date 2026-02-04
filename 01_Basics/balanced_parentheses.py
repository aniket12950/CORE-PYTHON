def is_balanced(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0

expr = "(())()"

if is_balanced(expr):
    print("Balanced Parentheses")
else:
    print("Not Balanced")
