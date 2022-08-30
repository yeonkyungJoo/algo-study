import sys

# sys.stdin = open("../input.txt", "rt")

K, N = map(int, input().split())
nums = []
for _ in range(K):
    nums.append(int(input()))

l, r = 0, max(nums)
answer = 0
while l <= r:
    m = (l + r) // 2

    cnt = 0
    for num in nums:
        cnt += num // m

    if cnt >= N:
        l = m + 1
        answer = max(answer, m)
    else:
        r = m - 1
print(answer)