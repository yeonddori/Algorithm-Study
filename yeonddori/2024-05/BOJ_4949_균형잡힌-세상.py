text = input()
while text != '.':
    stack = []
    answer = True
    for char in text:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] == '[':
                answer = False
                break
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] == '(':
                answer = False
                break
            stack.pop()
    if stack:
        answer = False
    print('yes' if answer else 'no')
    text = input()
