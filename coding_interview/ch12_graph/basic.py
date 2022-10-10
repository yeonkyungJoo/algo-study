from collections import deque

'''
def dfs(i, visited):
    visited.append(i)
    ch[i] = 1
    for k in graph[i]:
        if ch[k] == 0:
            visited = dfs(k, visited)
    return visited
'''
if __name__ == "__main__":
    graph = {
        1: [2, 3, 4],
        2: [5],
        3: [5],
        4: [],
        5: [6, 7],
        6: [],
        7: [3]
    }
    # 1. dfs(재귀)
    # ch = [0 for _ in range(8)]
    # print(dfs(1, []))

    # 2. dfs(스택)
    def _dfs(i):
        visited = []
        stack = [i]
        while stack:
            v = stack.pop()
            if v not in visited:
                visited.append(v)
                for x in graph[v]:
                    stack.append(x)
        return visited
    # print(_dfs(1))

    # 3. bfs(큐)
    def bfs(i):
        visited = [i]
        queue = deque()
        queue.append(i)
        while queue:
            v = queue.popleft()
            for x in graph[v]:
                if x not in visited:
                    visited.append(x)
                    queue.append(x)
        return visited
    print(bfs(1))