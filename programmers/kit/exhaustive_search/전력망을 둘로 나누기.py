import sys


def solution(n, wires):
    answer = sys.maxsize

    def dfs(v, count):
        if v in graph:
            for m in graph[v]:
                if ch[m - 1] == 0:
                    ch[m - 1] = 1
                    count = dfs(m, count + 1)
        return count

    graph = dict()
    for v1, v2 in wires:

        if v1 not in graph:
            graph[v1] = []
        graph[v1].append(v2)

        if v2 not in graph:
            graph[v2] = []
        graph[v2].append(v1)

    for v1, v2 in wires:
        ch = [0 for _ in range(n)]
        ch[v1 - 1] = 1
        ch[v2 - 1] = 1
        answer = min(answer, abs(dfs(v1, 1) - dfs(v2, 1)))
    return answer


if __name__ == "__main__":
    n = 4
    wires = [[1,2],[2,3],[3,4]]
    print(solution(n, wires))
