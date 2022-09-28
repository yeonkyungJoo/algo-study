import sys

# sys.stdin = open("../input.txt", "rt")
N = int(input())
nums = list(map(int, input().split()))

ch = [0 for _ in range(N)]


def dfs(i):
    global answer
    if i == N:
        l = []
        r = []
        for k in range(N):
            if ch[k] == 1:
                l.append(nums[k])
            else:
                r.append(nums[k])
        if sum(l) == sum(r):
            answer = 'YES'
        return
    ch[i] = 1
    dfs(i + 1)
    ch[i] = 0
    dfs(i + 1)


if __name__ == "__main__":
    answer = 'NO'
    dfs(0)
    print(answer)
