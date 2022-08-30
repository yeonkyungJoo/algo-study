import sys
#sys.stdin = open("input.txt", "rt")

N, K = map(int, input().split())
# print(N, K)

answer = -1
i = 1
cnt = 0
while i <= N:
    if N % i == 0:
        cnt += 1
        if cnt == K:
            answer = i
            break
    i += 1

print(answer)

