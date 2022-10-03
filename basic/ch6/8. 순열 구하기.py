import sys


# sys.stdin = open("../input.txt", "rt")

def dfs(i):
    global cnt

    if i == M:
        cnt += 1
        for k in res:
            print(k, end=' ')
        print()
        return

    for n in range(1, N+1):
        if ch[n] == 0:
            ch[n] = 1
            res[i] = n
            dfs(i+1)
            ch[n] = 0


if __name__ == "__main__":
    N, M = map(int, input().split())
    cnt = 0
    res = [0 for _ in range(M)]
    ch = [0 for _ in range(N+1)]
    dfs(0)
    print(cnt)
