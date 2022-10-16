def solution(n, computers):
    graph = dict()
    for i in range(len(computers)):
        for j in range(len(computers[i])):

            if i == j:
                continue

            v = computers[i][j]
            if v == 1:
                if i + 1 not in graph:
                    graph[i + 1] = []
                graph[i + 1].append(j + 1)

    def dfs(n):

        if n in graph:
            for m in graph[n]:
                if ch[m - 1] == 0:
                    ch[m - 1] = 1
                    dfs(m)

    ch = [0 for _ in range(n)]
    answer = 0
    for k in range(1, n + 1):
        if ch[k - 1] == 0:
            answer += 1
            ch[k - 1] = 1
            dfs(k)

    return answer