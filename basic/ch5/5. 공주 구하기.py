from collections import deque
if __name__ == "__main__":
    N, K = map(int, input().split())

    queue = deque([i for i in range(1, N+1)])
    n = 1
    while len(queue) > 1:
        if n == K:
            queue.popleft()
            n = 1
        else:
            queue.append(queue.popleft())
            n += 1
    print(queue[0])

