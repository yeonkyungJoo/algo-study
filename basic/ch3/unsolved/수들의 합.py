import sys

# sys.stdin = open("../input.txt", "rt")

N, M = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0
_sum = [[0 for i in range(N)] for j in range(N)]

for i in range(N):

    if nums[i] > M:
        continue

    if nums[i] == M:
        answer += 1
        continue

    elif nums[i] < M:
        for j in range(i, N):
            _sum[i][j] = _sum[i][j-1] + nums[j]

            if _sum[i][j] == M:
                answer += 1
            if _sum[i][j] >= M:
                break
print(answer)
'''
for i in range(N):
    for j in range(i, N):
        _sum = sum(nums[i:j+1])
        if _sum > M:
            break
        if _sum == M:
            answer += 1
            break
print(answer)
'''