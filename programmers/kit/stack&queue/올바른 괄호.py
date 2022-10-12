from collections import deque
def solution(s):

    if len(s) == 0:
        return True
    if len(s) % 2 != 0:
        return False

    stack = []
    queue = deque(s)
    while queue:
        c = queue.popleft()
        if c == '(':
            stack.append(c)
        else:
            if not stack or stack[-1] != '(':
                return False
            else:
                stack.pop()

    if len(stack) != 0:
        return False
    return True

if __name__ == "__main__":
    s = "(()("
    print(solution(s))