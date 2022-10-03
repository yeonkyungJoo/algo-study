# sys.stdin = open("../input.txt", "rt")

def dfs(i, _sum):

    answer.add(abs(_sum))
    if i >= K:
        return

    dfs(i+1, _sum + weights[i])
    dfs(i+1, _sum)
    dfs(i+1, _sum - weights[i])


if __name__ == "__main__":
    K = int(input())
    weights = list(map(int, input().split()))
    S = sum(weights)

    answer = set()
    dfs(0, 0)
    print((S + 1) - len(answer))