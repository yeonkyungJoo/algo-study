import sys

# sys.stdin = open("../input.txt", "rt")

N, C = map(int, input().split())
x = []
for _ in range(N):
    x.append(int(input()))
x.sort()

answer = 0
l, r = 0, max(x)
while l <= r:
    # 두 말 사이 거리
    m = (l + r) // 2

    cnt = 1
    cur = 0
    for p in range(1, N):
        if x[p] - x[cur] >= m:
            cnt += 1
            cur = p

    if cnt >= C:
        l = m + 1
        answer = max(answer, m)
    else:
        r = m - 1
print(answer)