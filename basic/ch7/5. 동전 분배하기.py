# sys.stdin = open("../input.txt", "rt")
import sys


def dfs(i, a, b, c):
    global answer

    if i == N:
        if a < b < c:
            answer = min(answer, c - a)
        return

    dfs(i+1, a + coins[i], b, c)
    dfs(i+1, a, b + coins[i], c)
    dfs(i+1, a, b, c + coins[i])

if __name__ == "__main__":
    N = int(input())
    coins = []
    for _ in range(N):
        coin = int(input())
        coins.append(coin)

    answer = sys.maxsize
    dfs(0, 0, 0, 0)
    print(answer)
