import sys

# sys.stdin = open("../input.txt", "rt")
N = int(input())
nums = [n for n in range(1, N + 1)]
# print(nums)


ch = [0 for _ in range(N)]


def dfs(i):
    if i == N:
        for j in range(N):
            if ch[j] == 1:
                print(nums[j], end=' ')
        print()
        return

    ch[i] = 1
    dfs(i + 1)
    ch[i] = 0
    dfs(i + 1)


if __name__ == "__main__":
    dfs(0)
