import sys


def dfs(idx, start):
    global answer
    if idx == M:
        dist = 0
        for hx, hy in house:
            _min = sys.maxsize
            for px, py in chosen:
                _min = min(_min, abs(px-hx) + abs(py-hy))
            dist += _min
        answer = min(answer, dist)
        return

    for k in range(start, len(pizza)):
        x, y = pizza[k]
        if ch[x][y] == 0:
            ch[x][y] = 1
            chosen.append((x, y))
            dfs(idx+1, k+1)
            chosen.pop()
            ch[x][y] = 0

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    ch = [[0 for _ in range(N)] for _ in range(N)]

    answer = sys.maxsize
    pizza = []
    house = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                house.append((i, j))
            if arr[i][j] == 2:
                pizza.append((i, j))
    chosen = []
    dfs(0, 0)
    print(answer)
