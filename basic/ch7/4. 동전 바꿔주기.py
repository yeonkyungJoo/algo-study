# sys.stdin = open("../input.txt", "rt")

def dfs(i, _sum):
    global cnt

    if _sum > T:
        return

    if i == k:
        if _sum == T:
            cnt += 1
        return

    for n in range(coins[i][1] + 1):
        dfs(i + 1, _sum + (coins[i][0] * n))


if __name__ == "__main__":
    T = int(input())
    k = int(input())
    coins = []
    for _ in range(k):
        coin, num = map(int, input().split())
        coins.append((coin, num))
    cnt = 0
    dfs(0, 0)
    print(cnt)
