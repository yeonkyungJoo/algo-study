import sys


# sys.stdin = open("../input.txt", "rt")

def dfs(i, start_idx, _sum):
    global cnt

    if i == K:
        if _sum % M == 0:
           cnt += 1
        return

    for j in range(start_idx, N):
        dfs(i+1, j+1, _sum + nums[j])

if __name__ == "__main__":
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    M = int(input())
    cnt = 0
    dfs(0, 0, 0)
    print(cnt)