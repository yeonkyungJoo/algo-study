import sys
from collections import deque

if __name__ == "__main__":
    M, N = map(int, input().split())
    arr = []
    exist = False
    for _ in range(N):
        _list = list(map(int, input().split()))
        arr.append(_list)
        if 0 in _list:
            exist = True

    if exist:

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        answer = sys.maxsize

        queue = deque()
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 1:
                    queue.append((i, j))

        cnt = 0
        while queue:
            x, y = queue.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] + 1
                    queue.append((nx, ny))
                    cnt = max(arr[nx][ny], cnt)

        answer = min(answer, cnt) - 1
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    answer = -1

    else:
        answer = 0
    print(answer)
