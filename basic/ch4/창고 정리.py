import sys

# sys.stdin = open("../input.txt", "rt")

L = int(input())
nums = list(map(int, input().split()))
M = int(input())

i = 1
while i <= M:

    _max, _min = 0, sys.maxsize
    _max_idx, _min_idx = -1, -1
    for j in range(L):

        if _max <= nums[j]:
            _max = nums[j]
            _max_idx = j
        if _min >= nums[j]:
            _min = nums[j]
            _min_idx = j
    nums[_max_idx] -= 1
    nums[_min_idx] += 1

    i += 1
print(max(nums) - min(nums))