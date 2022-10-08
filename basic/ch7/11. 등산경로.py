import sys
def dfs(x, y):
    global answer

    if x == dst[1][0] and y == dst[1][1]:
        answer += 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and ch[nx][ny] == 0 and arr[x][y] < arr[nx][ny]:
            ch[nx][ny] = 1
            dfs(nx, ny)
            ch[nx][ny] = 0


if __name__ == "__main__":
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    ch = [[0 for _ in range(N)] for _ in range(N)]
    src = [sys.maxsize, (0, 0)]
    dst = [-sys.maxsize, (0, 0)]
    for i in range(N):
        for j in range(N):
            if src[0] > arr[i][j]:
                src[0] = arr[i][j]
                src[1] = (i, j)
            if dst[0] < arr[i][j]:
                dst[0] = arr[i][j]
                dst[1] = (i, j)

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    answer = 0
    ch[src[1][0]][src[1][1]] = 1
    dfs(src[1][0], src[1][1])
    print(answer)