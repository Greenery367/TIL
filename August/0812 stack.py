def is_brakets(text):
    stack = []

    for char in text:
        if char == '(':
            stack.append(char)
        elif char == ')': 
            if not stack :
                return False
            stack.pop()
    return len(stack) == 0