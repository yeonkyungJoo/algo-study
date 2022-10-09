from collections import deque
if __name__ == "__main__":
    queue = deque(input())

    stack = []
    cnt = 0
    while queue:
        c = queue.popleft()
        if c == '(':
            stack.append(0)
        else: # ')'
            if stack and stack[-1] == 0:
                stack.pop()
                for i in range(len(stack)):
                    stack[i] += 1
            elif stack and stack[-1] != 0:
                n = stack.pop()
                cnt += n + 1
    print(cnt)
