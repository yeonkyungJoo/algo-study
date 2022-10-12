# sys.stdin = open("../input.txt", "rt")
import sys
from collections import deque

if __name__ == "__main__":
    N = 7
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    queue = deque()
    queue.append((0, 0))
    arr[0][0] = 0
    answer = -1
    while queue:
        i, j = queue.popleft()
        if i == N-1 and j == N-1:
            answer = arr[i][j]
            break
        for idx in range(4):
            _x = i + dx[idx]
            _y = j + dy[idx]
            if _x == 0 and _y == 0:
                continue
            if 0 <= _x < N and 0 <= _y < N and arr[_x][_y] == 0:
                arr[_x][_y] = arr[i][j] + 1
                queue.append((_x, _y))
    print(answer)