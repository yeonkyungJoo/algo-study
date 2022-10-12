from collections import deque
if __name__ == "__main__":
    N, M = input().split()
    queue = deque(map(int, list(N)))
    M = int(M)
    # print(N, M)

    stack = []
    while queue:
        n = queue.popleft()

        while stack and stack[-1] < n:
            if M == 0:
                break
            stack.pop()
            M -= 1
        stack.append(n)

    while M > 0:
        stack.pop()
        M -= 1
    print(''.join(map(str, stack)))


