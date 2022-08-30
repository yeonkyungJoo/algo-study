import sys
import math
#sys.stdin = open("input.txt", "rt")

N = int(input())
nums = [i for i in range(N+1)]

nums[1] = 0
for idx in range(2, int(math.sqrt(N+1)) + 1):
    num = nums[idx]
    if num != 0:
        for i in range(idx+num, N+1, num):
            nums[i] = 0
answer = 0
for num in nums:
    if num != 0:
        answer += 1
print(answer)
