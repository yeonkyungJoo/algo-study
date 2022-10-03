import sys


# sys.stdin = open("../input.txt", "rt")

def dfs(i):

    if i == N:
        temp = 0
        for k in range(N):
            temp += b[k] * res[k]
        if temp == F:
            print(' '. join(list(map(str, res))))
            sys.exit(0)

    for n in range(1, N+1):
        if ch[n] == 0:
            ch[n] = 1
            res[i] = n
            dfs(i+1)
            ch[n] = 0


if __name__ == "__main__":
    N, F = map(int, input().split())

    b = [1 for _ in range(N)]
    m = N-1
    d = 1
    for i in range(1, N-1):
        b[i] = b[i-1] * m
        b[i] = b[i] // d
        m -= 1
        d += 1
    res = [0 for _ in range(N)]
    ch = [0 for _ in range(N+1)]
    dfs(0)