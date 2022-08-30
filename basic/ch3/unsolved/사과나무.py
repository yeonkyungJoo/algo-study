import sys

# sys.stdin = open("../input.txt", "rt")

N = int(input())
nums = []
for _ in range(N):
    nums.append(list(map(int, input().split())))
# print(nums)

'''
2
1, 3
0, 4
1, 3
2
'''
i = 0
n = (N // 2)
answer = 0
while i <= n:
    for j in range(n - i, (n+1) + i):
        answer += nums[i][j]
    i += 1

i = 0
while i < n:
    for j in range(n - i, (n+1) + i):
        answer += nums[(N-1) - i][j]
    i += 1
print(answer)

