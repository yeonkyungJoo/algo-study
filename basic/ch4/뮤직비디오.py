import sys

# sys.stdin = open("../input.txt", "rt")

N, M = map(int, input().split())
musics = list(map(int, input().split()))

answer = sum(musics)
l, r = max(musics), sum(musics)
while l <= r:
    m = (l + r) // 2

    cnt = 0
    tmp = 0
    i = 0
    while i < N:
        if tmp + musics[i] < m:
            tmp += musics[i]
        elif tmp + musics[i] > m:
            cnt += 1
            tmp = musics[i]
        else:
            cnt += 1
            tmp = 0
        i += 1
    if tmp > 0:
        cnt += 1

    if cnt <= M:
        r = m - 1
        answer = min(answer, m)
    elif cnt > M:
        l = m + 1
print(answer)