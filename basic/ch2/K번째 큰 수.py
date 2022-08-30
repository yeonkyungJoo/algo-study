import sys
#sys.stdin = open("input.txt", "rt")

N, K = map(int, input().split())
nums = list(map(int, input().split()))
sums = set()
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sums.add(nums[i] + nums[j] + nums[k])
_sums = list(sums)
_sums.sort()
print(_sums[K * (-1)])