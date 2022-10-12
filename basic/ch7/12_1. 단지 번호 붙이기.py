import sys
def dfs(x, y):
    global cnt
    cnt += 1
    arr[x][y] = -1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
            dfs(nx, ny)

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
                cnt = 0
                dfs(i, j)
                count.append(cnt)
    print(total)
    count.sort()
    for c in count:
        print(c)