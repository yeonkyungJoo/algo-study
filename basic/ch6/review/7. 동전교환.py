import sys

# sys.stdin = open("../input.txt", "rt")

def dfs(n, _sum):
    global answer

    if n >= answer:
        return

    if _sum > M:
        return
    if _sum == M:
        answer = min(answer, n)
        return

    for i in range(N):
        dfs(n+1, _sum + coins[i])


if __name__ == "__main__":
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    coins.sort(reverse=True)
    res = [0 for _ in range(N)]
    answer = sys.maxsize
    dfs(0, 0)
    print(answer)
