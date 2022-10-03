import sys


# sys.stdin = open("../input.txt", "rt")
def dfs(i, _sum, tsum):
    global answer

    if _sum > C:
        return

    if _sum + (total - tsum) < answer:
        return

    if i == N:
        answer = max(_sum, answer)
        return

    dfs(i+1, _sum+weights[i], tsum+weights[i])
    dfs(i+1, _sum, tsum+weights[i])

if __name__ == "__main__":
    C, N = map(int, input().split())
    weights = []
    total = 0
    for _ in range(N):
        w = int(input())
        weights.append(w)
        total += w
    answer = 0
    ch = [0 for _ in range(N)]
    dfs(0, 0, 0)
    print(answer)