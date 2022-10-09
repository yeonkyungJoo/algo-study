import sys
from collections import deque

if __name__ == "__main__":
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))


    max_height = 1
    for i in range(N):
        for j in range(N):
            max_height = max(max_height, arr[i][j])
    # print(max_height)

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    answer = 0
    for h in range(1, max_height+1):
        cnt = 0
        arr_copy = [[arr[i][j] for j in range(len(arr[i]))] for i in range(len(arr))]
        for i in range(N):
            for j in range(N):
                if arr_copy[i][j] > h:

                    queue = deque()
                    queue.append((i, j))
                    arr_copy[i][j] = -1
                    cnt += 1
                    while queue:
                        x, y = queue.popleft()
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if 0 <= nx < N and 0 <= ny < N and arr_copy[nx][ny] > h:
                                arr_copy[nx][ny] = -1
                                queue.append((nx, ny))
        answer = max(answer, cnt)
    print(answer)