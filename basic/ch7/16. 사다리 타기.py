import sys

dx = [0, 0, -1]
dy = [-1, 1, 0]


def dfs(x, y):
    global answer

    if x == 0:
        answer = y
        return

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 10 and 0 <= ny < 10 and arr[nx][ny] == 1 and ch[nx][ny] == 0:
            ch[nx][ny] = 1
            dfs(nx, ny)
            ch[nx][ny] = 0
            break


if __name__ == "__main__":
    arr = []
    for _ in range(10):
        arr.append(list(map(int, input().split())))
    ch = [[0 for _ in range(10)] for _ in range(10)]
    src = -1
    for j in range(10):
        if arr[9][j] == 2:
            src = j
    answer = -1
    dfs(9, src)
    print(answer)
