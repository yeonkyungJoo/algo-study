import sys

# sys.stdin = open("../input.txt", "rt")

N = int(input())
nums = []
for _ in range(N):
    nums.append(list(map(int, input().split())))
# print(nums)

answer = 0
# 각 행의 합
for i in range(N):
    tmp = 0
    for j in range(N):
        tmp += nums[i][j]
    answer = max(answer, tmp)

# 각 열의 합
for j in range(N):
    tmp = 0
    for i in range(N):
        tmp += nums[i][j]
    answer = max(answer, tmp)

# 각 대각선의 합
tmp = 0
for i in range(N):
    tmp += nums[i][i]
answer = max(answer, tmp)

tmp = 0
for i in range(N):
    tmp += nums[N - (i+1)][i]
answer = max(answer, tmp)

print(answer)