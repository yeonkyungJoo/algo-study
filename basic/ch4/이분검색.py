import sys

# sys.stdin = open("../input.txt", "rt")

N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
l, r = 0, N - 1
while l <= r:
    m = (l + r) // 2
    if nums[m] < M:
        l = m + 1
    elif nums[m] > M:
        r = m - 1
    else:
        print(m+1)
        break
