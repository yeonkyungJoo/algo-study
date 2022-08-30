import sys
# sys.stdin = open("input.txt", "rt")

T = int(input())
for i in range(1, T+1):
    N, s, e, k = map(int, input().split())
    nums = list(map(int, input().split()))[s-1:e]
    # print(nums)
    nums.sort()
    print('#%d %d' %(i, nums[k-1]))