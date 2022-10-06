# sys.stdin = open("../input.txt", "rt")
import sys
from collections import deque

if __name__ == "__main__":
    S, E = map(int, input().split())
    dist = [-1 for i in range(10001)]
    queue = deque()

    queue.append(S)
    dist[S] = 0
    while queue:
        now = queue.popleft()
        if now == E:
            print(dist[now])
            break

        for k in [1, -1, 5]:
            if 0 < now + k < len(dist) and dist[now+k] == -1:
                dist[now + k] = (dist[now] + 1)
                queue.append(now+k)