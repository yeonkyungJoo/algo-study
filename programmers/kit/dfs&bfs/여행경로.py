from collections import deque


def solution(tickets):
    tickets.sort(key=lambda x: (x[0], x[1]))
    graph = dict()
    for ticket in tickets:
        src, dst = ticket
        if src not in graph:
            graph[src] = deque()
        graph[src].append(dst)

    answer = []

    def dfs(src, n, visit):
        nonlocal answer
        if n == len(tickets):
            answer = visit[:]
            return

        i = len(graph[src])
        while i > 0:
            if graph[src]:
                airport = graph[src].popleft()
                visit.append(airport)
                dfs(airport, n + 1, visit)
                # visit.pop()
                # graph[src].appendleft(airport)
            i -= 1

    visit = ['ICN']
    dfs('ICN', 0, visit)
    return answer