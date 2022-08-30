import sys

# sys.stdin = open("../input.txt", "rt")

n = int(input())
applicants = []
for _ in range(n):
    applicants.append(tuple(map(int, input().split())))

answer = 0
for i, (h, w) in enumerate(applicants):
    # print(i, h, w)
    for j, (_h, _w) in enumerate(applicants):
        if i == j:
            continue

        if h < _h and w < _w:
            break

    else:
        answer += 1
print(answer)

