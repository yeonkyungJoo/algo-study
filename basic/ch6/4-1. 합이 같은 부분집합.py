import sys

# sys.stdin = open("../input.txt", "rt")

def dfs(i, s):
    global total, answer

    if i == N:
        if (total - s) == s:
            answer = 'YES'
        return

    dfs(i+1, s+nums[i])
    dfs(i+1, s)


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))

    ch = [0 for _ in range(N)]
    total = sum(nums)
    answer = 'NO'
    dfs(0, 0)
    print(answer)
