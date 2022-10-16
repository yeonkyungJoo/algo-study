def solution(k, dungeons):
    def dfs(idx, k, cnt):
        nonlocal answer

        answer = max(answer, cnt)
        if idx == len(dungeons):
            return

        for i in range(len(dungeons)):
            if ch[i] == 0 and k >= dungeons[i][0]:
                ch[i] = 1
                dfs(idx + 1, k - dungeons[i][1], cnt + 1)
                ch[i] = 0

    answer = 0
    ch = [0 for _ in range(len(dungeons))]
    dfs(0, k, 0)

    return answer