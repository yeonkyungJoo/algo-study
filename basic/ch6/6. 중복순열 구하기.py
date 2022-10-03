import sys


# sys.stdin = open("../input.txt", "rt")

def dfs(i):
    global cnt

    if i == M:
        cnt = cnt + 1
        for n in res:
            print(n, end=' ')
        print()
        return

    for k in range(1, N+1):
        res[i] = k
        dfs(i+1)

if __name__ == "__main__":
    N, M = map(int, input().split())
    res = [0 for _ in range(M)]
    cnt = 0
    dfs(0)
    print(cnt)