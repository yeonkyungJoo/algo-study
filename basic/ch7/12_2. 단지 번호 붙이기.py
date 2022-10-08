import sys
from collections import deque

if __name__ == "__main__":
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, list(input()))))
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    total = 0
    count = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                total += 1

                queue = deque()
                queue.append((i, j))
                arr[i][j] = -1
                cnt = 1
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
                            arr[nx][ny] = -1
                            cnt += 1
                            queue.append((nx, ny))

                count.append(cnt)

    print(total)
    count.sort()
    for c in count:
        print(c)