# 깊이우선탐색
# 1, 2, 3, 4, 5, 6, 7

def dfs(n):
    if n > 7:
        return
    # 전위 순회
    # print(n, end=' ')
    # dfs(n * 2)
    # dfs(n * 2 + 1)

    # 중위 순회
    # dfs(n * 2)
    # print(n, end=' ')
    # dfs(n * 2 + 1)

    dfs(n * 2)
    dfs(n * 2 + 1)
    print(n, end=' ')

if __name__ == "__main__":
    dfs(1)
