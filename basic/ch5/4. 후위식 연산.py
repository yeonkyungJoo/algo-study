from collections import deque
if __name__ == "__main__":
    queue = deque(input())

    stack = []
    while queue:
        c = queue.popleft()
        if c.isnumeric():
            stack.append(int(c))
        else:
            n2 = stack.pop()
            n1 = stack.pop()

            if c == '+':
                stack.append(n1 + n2)
            elif c == '-':
                stack.append(n1 - n2)
            elif c == '*':
                stack.append(n1 * n2)
            elif c == '/':
                stack.append(n1 / n2)

    print(stack[0])