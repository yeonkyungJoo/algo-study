from collections import deque
if __name__ == "__main__":
    queue = deque(input())

    ops = []
    stack = []

    # 우선순위
    dic = {
        '(' : 0,
        ')' : 0,
        '+' : 1,
        '-' : 1,
        '*' : 2,
        '/' : 2
    }

    while queue:
        c = queue.popleft()
        if c.isnumeric():
            stack.append(c)
        else:
            if ops:
                if c == '(':
                    ops.append(c)
                elif c == ')':
                    while ops and ops[-1] != '(':
                        stack.append(ops.pop())
                    ops.pop()
                else:
                    while ops and ops[-1] != '(':
                        if dic[ops[-1]] >= dic[c]:
                            stack.append(ops.pop())
                        else:
                            break
                    ops.append(c)
            else:
                ops.append(c)
    while ops:
        stack.append(ops.pop())
    print(''.join(stack))
