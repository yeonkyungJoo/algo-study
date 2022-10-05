# sys.stdin = open("../input.txt", "rt")
import sys
from collections import deque

if __name__ == "__main__":
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    cnt = 0

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    queue = deque()
    queue.append((N // 2, N // 2))
    k = 0
    while k < N // 2:
        size = len(queue)
        for _ in range(size):
            i, j = queue.popleft()
            for idx in range(4):
                _x = i + dx[idx]
                _y = j + dy[idx]
                if 0 <= _x < N and 0 <= _y < N and arr[_x][_y] != -1:
                    cnt += arr[_x][_y]
                    arr[_x][_y] = -1
                    queue.append((_x, _y))
        k += 1
    print(cnt)
