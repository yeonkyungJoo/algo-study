# sys.stdin = open("../input.txt", "rt")

def dfs(i, total_profit):
    global answer

    if i > N:
        return
    answer = max(answer, total_profit)
    if i == N:
        return

    dfs(i + profits[i][0], total_profit + profits[i][1])
    dfs(i + 1, total_profit)


if __name__ == "__main__":
    N = int(input())
    profits = []
    for _ in range(N):
        T, P = map(int, input().split())
        profits.append((T, P))
    answer = 0
    dfs(0, 0)
    print(answer)
