# sys.stdin = open("../input.txt", "rt")
import sys

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):
    global answer

    if x == N-1 and y == N-1:
        answer += 1
        return
    for i in range(4):
        _x = x + dx[i]
        _y = y + dy[i]
        if 0 <= _x < N and 0 <= _y < N and arr[_x][_y] == 0:
            arr[x][y] = -1
            dfs(_x, _y)
            arr[x][y] = 0

if __name__ == "__main__":
    N = 7
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    answer = 0
    arr[0][0] = -1
    dfs(0, 0)
    print(answer)