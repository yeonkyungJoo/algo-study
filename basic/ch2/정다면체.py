import sys
#sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
sums = [0 for _ in range(N + M + 1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        sums[i+j] += 1
# print(sums)
_max = 0
answer = []
for idx, cnt in enumerate(sums):
    if _max < cnt:
        answer.clear()
        answer.append(idx)
        _max = cnt
    elif _max == cnt:
        answer.append(idx)
print(' '.join(map(str, answer)))
