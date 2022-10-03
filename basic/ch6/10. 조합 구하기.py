import sys


# sys.stdin = open("../input.txt", "rt")

def dfs(i, k):
    global cnt

    if i == M:
        print(' '.join(map(str, res)))
        cnt += 1
        return

    for n in range(k, N+1):
        res[i] = n
        dfs(i+1, n+1)


if __name__ == "__main__":
    N, M = map(int, input().split())
    cnt = 0
    res = [0 for _ in range(M)]
    dfs(0, 1)
    print(cnt)