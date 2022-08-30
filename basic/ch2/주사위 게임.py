import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())

answer = []
for _ in range(N):

    nums = list(map(int, input().split()))
    tmp = set(nums)
    if len(tmp) == 1:
        answer.append(10000 + tmp.pop() * 1000)
    elif len(tmp) == 2:
        answer.append(1000 + (sum(nums) - sum(tmp)) * 100)
    elif len(tmp) == 3:
        answer.append(max(tmp) * 100)

answer.sort(reverse=True)
print(answer[0])