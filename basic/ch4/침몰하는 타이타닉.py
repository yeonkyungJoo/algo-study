import sys
from collections import deque
# sys.stdin = open("../input.txt", "rt")

N, M = map(int, input().split())
weights = list(map(int, input().split()))
weights.sort()

weights = deque(weights)
answer = 0
while weights:

    if len(weights) == 1:
        answer += 1
        break

    if weights[0] + weights[-1] <= M:
        weights.pop()
        weights.popleft()
        answer += 1
    else:
        weights.pop()
        answer += 1

print(answer)