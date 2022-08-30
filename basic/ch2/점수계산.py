import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())
count = map(int, input().split())

score = [0 for _ in range(N)]
for idx, c in enumerate(count):
    if c == 1:
        if idx == 0:
            score[idx] = 1
        else:
            score[idx] += score[idx-1] + 1
print(sum(score))