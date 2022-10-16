from collections import deque
import sys


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = sys.maxsize

    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    graph = [[0 for _ in range(15)] for _ in range(15)]
    ch = [[0 for _ in range(15)] for _ in range(15)]
    for x1, y1, x2, y2 in rectangle:

        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                graph[i][j] = 1

        for y in [y1, y2]:
            for x in range(x1, x2 + 1):
                graph[y][x] = 2

        for x in [x1, x2]:
            for y in range(y1, y2 + 1):
                graph[y][x] = 2

    for i in range(len(graph)):
        print(graph[i])
    queue = deque()
    queue.append((characterX, characterY))
    ch[characterY][characterX] = 1
    while queue:
        x, y = queue.popleft()
        print(x, y, ch[y][x])
        if x == itemX and y == itemY:
            answer = min(answer, ch[y][x])
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 15 and 0 <= ny < 15 and graph[ny][nx] == 2:
                if ch[ny][nx] == 0:
                    ch[ny][nx] = ch[y][x] + 1
                    queue.append((nx, ny))

    return answer - 1


if __name__ == "__main__":
    rectangle = [[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]]
    characterX = 1
    characterY = 3
    itemX = 7
    itemY = 8
    print(solution(rectangle, characterX, characterY, itemX, itemY))
